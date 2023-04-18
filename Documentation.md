# IUNI Documentation
The IUNI framework is a comprehensive testing framework designed for developers and testers to write effective, reliable, and consistent test cases for their applications. It includes three main classes: `Unitester`, `APILoadTester`, and `SecurityTester`. The Unitester class provides a range of assertion methods to test different conditions. The APILoadTester class is designed to provide functionality for load testing a web API. It inherits from the Unitester class and includes attributes and methods for setting the base URL of the web API to be tested, HTTP headers to be included in each request, the number of concurrent requests to be made, and the duration of the load test in seconds. The SecurityTester class provides functionality for testing the security of a web application. It includes methods for running all security tests and adding a result to the results list.

# Uniteser
The `Unitester` class is a comprehensive testing framework that provides a variety of assertion methods to check conditions and raise an `AssertionError` if they are not met. The framework is designed to help developers and testers write effective, reliable and consistent test cases for their applications.

To use the `Unitester` class, you can instantiate it and define your test cases by calling the `test()` method. Each test case should be a function or method that you want to test. You can pass optional arguments or fixtures to the `test()` method to specify the test inputs and expected output.

After defining your test cases, you can call the `run()` method to run all the tests. The `run()` method handles any failures or errors that occur and stores the results in the passed and failed attributes. To view the test results, you can call the `summary()` method to print a summary of the test results to the console or call the `export_results()` method to export the results to a log file.

## Assertion Methods

The Unitester class provides a range of assertion methods to test different conditions. These assertion methods include:

* assert_equal(expected, actual, msg=None)
* assert_true(actual, msg=None)
* assert_false(actual, msg=None)
* assert_raises(expected_exception, callable, *args, **kwargs)
* assert_in(item, iterable, msg=None)
* assert_not_in(item, iterable, msg=None)
* assert_is(expected, actual, msg=None)
* assert_is_not(expected, actual, msg=None)
* assert_is_none(actual, msg=None)
* assert_is_not_none(actual, msg=None)
* assert_greater(first, second, msg=None)
* assert_greater_equal(first, second, msg=None)
* assert_less(first, second, msg=None)
* assert_less_equal(first, second, msg=None)
* assert_is_instance(obj, cls, msg=None)
* assert_not_is_instance(obj, cls, msg=None)
* assert_is_subtype(obj, cls, msg=None)
* assert_not_is_subtype(obj, cls, msg=None)
* assert_regex_match(pattern, string, msg=None)
* assert_regex_search(pattern, string, msg=None)
* assert_type(obj, typ, msg=None)
* assert_not_type(obj, typ, msg=None)

Each of these assertion methods can be used to test a specific condition in your application. If the condition is not met, the assertion method will raise an AssertionError and the test will fail.

---

# APILoadTester

The APILoadTester class is a part of the IUNI framework, designed to provide functionality for load testing a web API. This class inherits from the Unitester class, which provides basic functionality for unit testing. The APILoadTester class includes the following attributes and methods:

## Attributes

* **url (str):** The base URL of the web API to be tested.
* **headers (dict):** HTTP headers to be included in each request.
* **concurrency_level (int):** The number of concurrent requests to be made during the load test.
* **duration (float):** The duration of the load test in seconds.
* **requests (list):** A list of requests to be made during the load test.
* **results (dict):** A dictionary containing the results of the load test.
* **Methods**

`set_url(url)`
Sets the base URL of the web API to be tested.

* **url (str):** The base URL of the web API.
`set_headers(headers)`
Sets the HTTP headers to be included in each request.

* **headers (dict):** HTTP headers to be included in each request.
`set_concurrency_level(level)`
Sets the number of concurrent requests to be made during the load test.

* **level (int):** The number of concurrent requests to be made during the load test.
`set_duration(duration)`
Sets the duration of the load test in seconds.

**duration (float):** The duration of the load test in seconds.
`add_request(method, path, data=None, headers=None)`
Adds a request to the list of requests to be made during the load test.

* **method (str):** The HTTP method to use for the request.
`path (str): The path of the resource being requested.`
* **data (dict or str):** Data to be included in the request body (optional).
* **headers (dict):** HTTP headers to be included in the request (optional).
`run_load_test()`
Runs the load test and collects performance metrics.

* `print_results()`
Prints the results of the load test.

* `export_api_load(filename)`
Exports the results of the load test to a file.

* **filename (str):** The name of the file to be created. The file will be created in the current working directory and will have a .log extension.

---

# SecurityTester

The SecurityTester class provides functionality for testing the security of a web application. It has the following attributes:

## Attributes
* **target_url (str):** The base URL of the web application to be tested.
* **headers (dict):** HTTP headers to be included in each request.
* **cookies (dict):** Cookies to be included in each request.
* **results (list):** A list of dictionaries containing the results of each security test.
Methods
run_tests()

This method runs all security tests. It sends HTTP requests to the target URL and checks for common security vulnerabilities such as cross-site scripting (XSS), SQL injection, and others.

`add_result(test_name, status, description=None)`

This method adds a result to the results list. It takes three arguments:

* `test_name (str)`: The name of the test that was performed.
* `status (str)`: The status of the test, either "passed" or "failed".
* `description (str, optional)`: A description of the test result.

If no description is provided, the method will add an empty string as the description.

Example Usage
`from security_tester import SecurityTester`

# Create a SecurityTester instance with the target URL and headers
`tester = SecurityTester("https://example.com", {"User-Agent": "Mozilla/5.0"})`

# Run all security tests
`tester.run_tests()`

# Print the results
```
for result in tester.results:
    print(result["test_name"], result["status"], result["description"])
```
In this example, a SecurityTester instance is created with the target URL "https://example.com" and a custom User-Agent header. The run_tests() method is called to run all security tests, and the results are printed to the console.



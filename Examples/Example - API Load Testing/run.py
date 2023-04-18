from IUNI.IUNI import APILoadTester

load_test = APILoadTester()

load_test.set_url("https://jsonplaceholder.typicode.com")

load_test.set_headers({
    "Content-Type": "application/json"
})

load_test.set_concurrency_level(10)

load_test.set_duration(5)

load_test.add_request("GET", "/posts/1")

def handle_response(response):
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
    else:
        print(f"Response: {response.json()}")

def handle_error(path, error):
    print(f"Error encountered for path {path}: {error}")

load_test.handle_response = handle_response
load_test.handle_error = handle_error

load_test.run_load_test()
load_test.print_results()
load_test.export_api_load("load")

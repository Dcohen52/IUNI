from IUNI.IUNI import APILoadTester

# Create a new instance of the LoadTest class
load_test = APILoadTester()

# Set the base URL of the API to be tested
load_test.set_url("https://jsonplaceholder.typicode.com")

# Set the HTTP headers to be included in each request
load_test.set_headers({
    "Content-Type": "application/json"
})

# Set the number of concurrent requests to be made during the load test
load_test.set_concurrency_level(10)

# Set the duration of the load test in seconds
load_test.set_duration(5)

# Add a request to the list of requests to be made during the load test
load_test.add_request("GET", "/posts/1")


# Define a function to handle the response of each request
def handle_response(response):
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
    else:
        print(f"Response: {response.json()}")


# Define a function to handle errors encountered during the load test
def handle_error(path, error):
    print(f"Error encountered for path {path}: {error}")


# Add the handle_response and handle_error functions to the LoadTest instance
load_test.handle_response = handle_response
load_test.handle_error = handle_error

# Run the load test and print the results
load_test.run_load_test()
load_test.print_results()
load_test.export_api_load("load")

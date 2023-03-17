# IUNI Framework for Testing

The IUNI framework is a highly versatile and comprehensive testing framework designed to provide developers with a robust toolset for testing software code. The framework offers a unit testing, Web API performance testing and Security Testing modules.


## Getting Started
To begin using the IUNI framework, simply install it using pip in your terminal:

```pip install IUNI```

After installation, you can import the IUNI class and begin using its various assertion methods to test your code.

## Supported Features

### Unit Testing

The assertion methods included in the ```Unitester``` class are designed to test specific conditions, such as equality,
truthiness,
the presence of items in iterable objects, object types, regular expressions, and many more. These methods provide clear
and informative error messages, which help developers identify and fix issues in their code.

The ```Unitester``` class allows the definition of new tests using the ```test()``` method, and it provides a ```run()``` method to
execute all defined tests while handling any failures or errors that may occur.

In addition, the ```Unitester``` class offers a ```summary()``` method that displays a concise summary of the test
results,
including the
total number of tests, the number of passed and failed tests, and the names of the tests that failed. Furthermore, the
framework allows developers to export the test results to a file using the ```export_results()``` method.

### Web API Performance Testing

The ```APILoadTester``` class is part of the IUNI framework and provides functionality for load testing a web API. This class
can be used to simulate a high volume of concurrent requests to a web API and collect performance metrics, including
response time, throughput, and error rate.

### Security Testing

The ```SecurityTester``` class is designed to provide a simple and easy-to-use interface for testing the security of a
web
application. The class includes several methods that test for common security vulnerabilities, such as SQL injection,
cross-site scripting (XSS), command injection, and insecure direct object reference (IDOR).

To use the ```SecurityTester``` class, you simply need to create an instance of the class and pass in the URL of the web
application you wish to test, along with any necessary headers and cookies. Once you have created an instance of the
class, you can call the ```run_tests``` method to execute the security tests.

## Working on

* Easy-to-use and reliable UI testing class.

## Contribution

This project is open source, and contributions from the community are highly valued and appreciated. If you are
interested in contributing to the development of this project, please feel free to reach out or submit a pull request.

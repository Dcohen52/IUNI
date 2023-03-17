from IUNI.IUNI import Unitester
from functions import add, subtract, multiply, divide, fibonacci, factorial, is_prime, reverse_list, count_vowels, \
    flatten_list, is_palindrome, binary_search


# Simple arithmetics

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 0) == 0
    assert multiply(-1, 1) == -1


def test_divide():
    assert divide(6, 3) == 2
    assert divide(0, 1) == 0
    assert divide(-1, 1) == -1
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected divide by zero exception"


# Mathematical functions

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True
    assert is_prime(13) is True
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(8) is True  # should fail
    assert is_prime(9) is False
    assert is_prime(10) is False


def test_reverse_list():
    assert reverse_list([]) == []
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([1, [2, 3], 4, [5, [6, 7]]]) == [[5, [6, 7]], 4, [2, 3], 1]


def test_count_vowels():
    assert count_vowels("") == 0
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 6  # should fail
    assert count_vowels("xylophone") == 3


def test_flatten_list():
    assert flatten_list([]) == []
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    assert flatten_list([1, [2, 3], 4, [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7]


def test_is_palindrome():
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("racecar") is False  # should fail
    assert is_palindrome("abba") is True
    assert is_palindrome("not a palindrome") is False
    assert is_palindrome("hello world") is False


def test_binary_search():
    assert binary_search([], 1) is False
    assert binary_search([1, 2, 3, 4, 5], 1) is True
    assert binary_search([1, 2, 3, 4, 5], 3) is True
    assert binary_search([1, 2, 3, 4, 5], 5) is True
    assert binary_search([1, 2, 3, 4, 5], 0) is False
    assert binary_search([1, 2, 3, 4, 5], 6) is False


IUNI = Unitester()
IUNI.test(test_add)
IUNI.test(test_subtract)
IUNI.test(test_multiply)
IUNI.test(test_divide)
IUNI.test(test_fibonacci)
IUNI.test(test_factorial)
IUNI.test(test_is_prime)
IUNI.test(test_reverse_list)
IUNI.test(test_count_vowels)
IUNI.test(test_flatten_list)
IUNI.test(test_is_palindrome)
IUNI.test(test_binary_search)

IUNI.run()
IUNI.summary()
# IUNI.export_results("test")

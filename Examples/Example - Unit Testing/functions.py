# Simple arithmetics

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Math functions
def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Lists & Strings

def reverse_list(lst):
    return lst[::-1]


def count_vowels(word):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in word if char in vowels)


def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def is_palindrome(word):
    return word == word[::-1]


def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

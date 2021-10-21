"""
In this challenge, you have to establish if a given integer n is a Sastry number. If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number. Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not. A perfect square is a number with a square root equals to a whole integer. You can expect only valid positive integers greater than 0 as input, without exceptions to handle. Zero is a perfect square, but the concatenation 00 isn't considered as a valid result to check.
"""

import math


def is_sastry(num):
    coeff = 1
    temp = num  # create a copy of the number

    # calculate the successor early because
    # the value contained in num is about to
    # change
    successor = num + 1

    # this is a quick way to scale the
    # original number by the appropriate
    # number of digits
    while temp:
        num *= 10
        temp //= 10

    num += successor

    root = int(math.sqrt(num))

    return root ** 2 == num


ans1 = is_sastry(183)
exp1 = (
    True  # Concatenation of n and its successor = 183184 is a perfect square (428 ^ 2)
)
assert ans1 == exp1, f"Expected {exp1}, got {ans1}"

ans2 = is_sastry(184)
exp2 = False  # Concatenation of n and its successor = 184185 is not a perfect square
assert ans2 == exp2, f"Expected {exp2}, got {ans2}"

ans3 = is_sastry(106755)
exp3 = True  # Concatenation of n and its successor = 106755106756 is a perfect square (326734 ^ 2)
assert ans3 == exp3, f"Expected {exp3}, got {ans3}"

print("Everything okay")

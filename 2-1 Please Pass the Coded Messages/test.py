#!/usr/bin/python
from solution import solution

print("TEST CASE 1")
assert(solution([3, 1, 4, 1]) == 4311)

print("TEST CASE 2")
assert(solution([3, 1, 4, 1, 5, 9]) == 94311)

print("TEST CASE 3")
assert(solution([1, 1]) == 0)

print("TEST CASE 4")
assert(solution([0, 3]) == 30)

print("TEST CASE 5")
assert(solution([0, 0]) == 0)

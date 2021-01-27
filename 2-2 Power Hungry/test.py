#!/usr/bin/python
from solution import solution

print("TEST CASE 1")
assert(solution([2,0,2,2,0]) == "8")

print("TEST CASE 2")
assert(solution([-2, -3, 4, -5]) == "60")

print("TEST CASE 3")
assert(solution([-4,-2,-3,6]) == "72")

print("TEST CASE 4")
assert(solution([1,-17]) == "1")

print("TEST CASE 5")
assert(solution([-1000]) == "-1000")

print("TEST CASE 6")
assert(solution([-1000, 0]) == "0")

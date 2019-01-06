"""
Thought On The Question:
Difficulty: Medium/Easy
Strategy:
This is a pure mathematical question.
Using the property of the modulus, we can separate the equation into two parts:
1^b + 2^b + ... + (a//2)^b and a^b + (a-1)^b + (a-2)^b +...+(a//2+1)^b if a is odd
in this case, all those modulus cancel out and gives 0
if a is even, then everything cancels out except the middle number (a//2)^b
so we just need to find the middle number and then find the modulus of that number
"""

import sys

a, b = sys.stdin.readline().strip().split()

a = int(a)
b = int(b)

def find_mod(a,b):
    if (a-1) % 2 == 0:
        return 0
    else:
        k = a // 2
        result = (k ** b) % a

        return result

print(find_mod(a,b))
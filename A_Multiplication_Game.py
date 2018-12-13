"""
Thought on the question:
Difficulty: Medium.
To boil down the question: there are certain intervals which either Stan or Ollie are bound to win:
k is ceil(log(n,18))
if it is between (18^(k-1),18^k /2], Stan wins
if it is between [18^k /2,18^k), Ollie wins
"""
import sys
import math

n = []

for line in sys.stdin:
    try:
        line = int(line.strip("\n"))
        n.append(int(line))
    except:
        break


for i in range(len(n)):
    k = math.log(n[i], 18)
    if abs(k - int(k)) < 0.1**7: # this is to iron out the error of python
        k = int(k)
    else:
        k = math.ceil(k)
    num = 18 ** k
    if num // 2 < n[i] <= num:
        print("Ollie wins.")
    else:
        print("Stan wins.")



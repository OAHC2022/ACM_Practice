"""
Thought on the question:
Difficulty: Easy.
"""
import sys

fl = sys.stdin.readline().strip().split()
sl = list(sys.stdin.readline().strip())
fl_b = fl.copy()
for i in range(3):
    fl[i] = int(fl[i])
fl_b[sl.index("A")] = str(min(fl))
del fl[fl.index(min(fl))]
fl_b[sl.index("B")] = str(min(fl))
del fl[fl.index(min(fl))]
fl_b[sl.index("C")] = str(min(fl))
ans = " ".join(fl_b)
print(ans)


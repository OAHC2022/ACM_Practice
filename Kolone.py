"""
Thought on the question:
Difficulty: Easy.
The position of each ant in the second row can be calculated according to the length of the first row and the value T
Insert the ant from the second row to the first row
"""
import sys

a1_l, a2_l = sys.stdin.readline().strip().split()
ant1 = list(sys.stdin.readline().strip())
ant2 = list(sys.stdin.readline().strip())
T = int(sys.stdin.readline())
ant1 = ant1[::-1]
a1_l = int(a1_l)
a2_l = int(a2_l)


def find_it():
    global ant1
    global ant2
    if T >= a1_l + a2_l:
        final = ant2 + ant1
        return "".join(final)
    final = ant1
    count = 0
    for i in range(a2_l):
        if a1_l - (T - i) < 0:
            final.insert(i, ant2.pop(0))
            count += 1
        else:
            final.insert(a1_l - (T - i) + count, ant2.pop(0))
            count += 1
    return "".join(final)


print(find_it())

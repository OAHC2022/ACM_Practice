"""
Thought on the question:
Difficulty: Easy.
Since using bigger paper first will save the tape,
the strategy is to traverse through the list first, finding the enough material to make a A1
Then find the tape needed to seal the papers
"""
import sys

n = int(sys.stdin.readline().strip()) - 1
A = sys.stdin.readline().strip().split()
length = 2 ** (-3 / 4)
width = 2 ** (-5 / 4)

for i in range(n):
    A[i] = int(A[i])


def get_index():
    count = 0
    for i in range(n):
        count *= 2
        count += A[i]
        if count >= 2 ** (i + 1):
            A[i] = A[i] - (count - 2 ** (i + 1))
            return i + 1
    print("impossible")
    sys.exit()


index = get_index()
tape = 0
for k in range(index):
    # do the first and the do the last
    forward = 0
    if (index - k) % 2 == 1:
        # length
        forward = A[index - k - 1] // 2
        tape += (length / (2 ** ((index - k) // 2))) * forward

    elif (index - k) % 2 == 0:
        forward = A[index - k - 1] // 2
        tape += (width / (2 ** ((index - k) // 2 - 1))) * forward

    if A[index - k - 1] != 0:
        A[index - k - 2] += forward

print(tape)

# Watkins, jmw4dx
in_line = input().strip().split(" ")
N, M, A, C, X_0 = [int(i) for i in in_line]

sequence = [0] * (N+1)
sequence[0] = X_0
for i in range(N):
    sequence[i+1] = (A*sequence[i] + C) % M

sequence.pop(0)
# print(sequence)

def binary_search(value, start, end, index):
    if (start > end):
        return -1
    mid = (start+end) // 2
    if sequence[mid] == value:
        return mid
    elif sequence[mid] < value: # go right
        if index < mid:
            return -1
        return binary_search(value, mid+1, end, index)
    elif sequence[mid] > value: # go left
        if index > mid:
            return -1
        return binary_search(value, start, mid - 1, index)
    # issue
    return -1

total = 0
for i in range(N):
    val = sequence[i]
    index = binary_search(val, 0, N-1, i)
    if index != -1:
        total += 1

print(total)

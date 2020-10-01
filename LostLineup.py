# Watkins, jmw4dx
N = int(input().strip())
distances = input().strip().split(" ")
# '''
# 4
# A-1 B-2 C-0
# A - 2
# B - 3
# C - 4
#
# Jimmy C A B
# '''

mapping = [0] * (N-1)

for i in range(N-1):
    dist = int(distances[i])
    mapping[dist] = i+2

# '''
# 1 - 2
# 2 - 3
# 0 - 4
# '''

answer = ["1"]*N
for i in range(N-1):
    answer[i+1] = str(mapping[i])

print(" ".join(answer))
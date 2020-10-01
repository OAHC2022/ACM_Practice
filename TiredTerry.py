# Watkins, jmw4dx
in_line = input().strip().split(" ")
N, P, D = int(in_line[0]), int(in_line[1]), int(in_line[2])

pattern = input().strip()
'''
WZWWZ|WZWWZ
N=5,P=3,D=2
from i - p + 1 to i
let i = 4
4 - 3 + 1 = 2
2, 3, 4
'''

def conv(j):
    return (j + N) % N

totalTired = 0
# print(N, P, D)
totalSleep = 0
for j in range(0, P):
    if pattern[conv(j)] == "Z":
        totalSleep += 1
if totalSleep < D:
    totalTired += 1

for i in range(1, N):
    dropOff = i - 1
    pickUp = i + P - 1
    if pattern[conv(dropOff)] == "Z":
        totalSleep -= 1
    if pattern[conv(pickUp)] == "Z":
        totalSleep += 1
    if totalSleep < D:
        totalTired += 1

# for i in range(N):
#     totalSleep = 0
#     for j in range(i, i+P):
#         # print(i, j, conv(j))
#         if pattern[conv(j)] == "Z":
#             totalSleep += 1
#     # print(i, totalSleep)
#     if totalSleep < D:
#         totalTired += 1

print(totalTired)
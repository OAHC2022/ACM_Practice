# Watkins, jmw4dx
N = int(input())

opus = [int(k) for k in input().strip().split(" ")]

profsLeft = list(range(1, N+1)) # = [1, 2, 3, 4, ..., N]

i = 0
while len(profsLeft) > 1:
    i = i % len(profsLeft)
    incr = opus[profsLeft[i] - 1] # prof 3's opus is stored at opus[2]
    i = (i + incr - 1) % len(profsLeft)
    profsLeft.pop(i)

print(profsLeft[0])

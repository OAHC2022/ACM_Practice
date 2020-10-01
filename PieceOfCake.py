# Watkins, jmw4dx
in_line = input().split(" ")
N, H, V = int(in_line[0]), int(in_line[1]), int(in_line[2])

side1 = max(H, N-H)
side2 = max(V, N-V)

print(side1*side2*4)
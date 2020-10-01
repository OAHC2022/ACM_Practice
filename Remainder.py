# Watkins, jmw4dx
A, B, C, D, E, F, G = [int(i) for i in input().strip().split(" ")]
import math

c = A*B
b = -(4*A + 4*B)
a = 12
x = int(round((-b-math.sqrt(b**2 - 4*a*c))/(2*a)))

options = list(range(max(x-3, 1), min(x+3, A//2) + 1, 1))
volumes = [(A-2*o)*(B-2*o)*o for o in options]
combined = [(volumes[i], options[i]) for i in range(len(options))]
combined = sorted(combined, reverse=True)
best1, best2, best3 = combined[0:3]
v1, x1 = best1
v2, x2 = best2
v3, x3 = best3

val1 = math.ceil((F-C)/v1) * v1 + C
val2 = math.ceil((F-D)/v2) * v2 + D
val3 = math.ceil((F-E)/v3) * v3 + E

# maxVal1 = math.floor((G-C)/v1) * v1
# maxVal2 = math.floor((G-D)/v2) * v2
# maxVal3 = math.floor((G-E)/v3) * v3
#print(v1, v2, v3)
#print(C, D, E)
#print(val1, val2, val3)

while (not( val1 == val2 and val2 == val3) and max(val1, val2, val3) <= G):
    m = min(val1, val2, val3)
    if val1 == m:
        val1 += v1
    elif val2 == m:
        val2 += v2
    else:
        val3 += v3
    #print(val1, val2, val3)

if (val1 == val2 and val2 == val3):
    print(val1)
else:
    print("ERROR")
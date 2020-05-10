# Modular Exponentiation Algorithm
# dynamic programming:
# Power(x,y) = 
#    -
#    |   1                    if y == 0
#   <    Power(x^2, y//2)     if y % 2 == 0
#    |   x* Power(x^2, y//2)  if y % 2 == 1
#    -

def modular_exp(x,y,m):
    if y == 0:
        return 1
    x = x % m
    result = 1
    while y > 0:
        if y % 2:
            result = (x * result) % m
        x = (x * x) % m
        y = y // 2
    return result

m = 10**9 + 7
print(modular_exp(34543987529435983745230948023948,3498573497543987543985743989120393097595572309482304,m))

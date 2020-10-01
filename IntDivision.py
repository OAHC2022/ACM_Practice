# Watkins, jmw4dx
in_line = input().strip().split(" ")

N, D = int(in_line[0]), int(in_line[1])

nums = [int(i)//D for i in input().strip().split(" ")]

total = 0

duplicates = dict()
for num in nums:
    if num not in duplicates.keys():
        duplicates[num] = 1
    else:
        duplicates[num] += 1

# print(duplicates)

def fancy(x):
    return (x+1)*(x)//2

for key in duplicates.keys():
    total += fancy(duplicates[key] - 1)
# print(sorted(nums))
#
# for i in range(N-1):
#     for j in range(i+1, N):
#         if nums[i] == nums[j]:
#             total += 1

print(total)

# def func(x):
#     if x == 0:
#         return 0
#     else:
#         return x + func(x-1)



# for i in range(1, 10):
#     print(i, func(i-1), func2(i-1))
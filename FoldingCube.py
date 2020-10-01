# Watkins, jmw4dx
components = []
for i in range(6):
    components.append([c for c in input().strip()])

# print("old")
# for row in components:
#     print("".join(row))

def getR(row):
    return components[row]

def getC(column):
    c = []
    for row in components:
        c.append(row[column])
    return c

def get(row, column):
    return components[row][column]

def chainRow(row):
    top = 0
    currTop = 0
    for i in range(6):
        if components[row][i] == "#":
            currTop += 1
        else:
            top = max(top, currTop)
            currTop = 0
    return max(top, currTop)

def chainColumn(column):
    top = 0
    currTop = 0
    for i in range(6):
        if components[i][column] == "#":
            currTop += 1
        else:
            top = max(top, currTop)
            currTop = 0
    return max(top, currTop)


while (getR(0) == ['.', '.', '.', '.', '.', '.']):
    components.pop(0)
    components.append(['.', '.', '.', '.', '.', '.'])

while (getC(0) == ['.', '.', '.', '.', '.', '.']):
    for row in components:
        row.pop(0)
        row.append('.')

print("new")
for i in range(6):
    print("".join(getR(i)), chainRow(i))

print("".join([str(chainColumn(i)) for i in range(6)]))

longR = [chainRow(i) for i in range(6)]
longC = [chainColumn(i) for i in range(6)]

answer = False
for nums in [longR, longC]:
    if nums[0:3] in [[2,3,1], [1,3,2], [1,4,1], [3,3,0]]:
        answer = True

for nums1, nums2 in [[longR, longC], [longC, longR]]:
    if nums1[0:3] == [2,2,2] and nums2[0:4] == [1,2,2,1]:
        answer = True

options = {
    False: "cannot fold",
    True: "can fold"
}

print(options[answer])
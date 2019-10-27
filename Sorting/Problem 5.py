r,c = [int(x) for x in input().split()]
matrix = []
for row in range(r):
    a = []
    a = [int(x) for x in input().split()]
    matrix.append(a)

temp = []
for row in matrix:
    for item in row:
        temp.append(item)

temp.sort()
i = 0
for row in range(r):
    for col in range(c):
        print(temp[i], end=" ")
        i += 1
    print()
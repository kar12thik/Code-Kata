len1 , len2 = [int(x) for x in input().split()]
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
freq = {}
for item in l1:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

temp = []
for num in l2:
    for item,value in freq.items():
        if num == item:
            for times in range(value):
                temp.append(num)

temp2 = []
for item in l1:
    if item not in temp:
        temp2.append(item)

temp2.sort()
temp += temp2
for x in temp:
    print(x,end=' ')

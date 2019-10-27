def altsort(arr,length):
    l2 = list()
    for num in range(0,length,2):
        l2.append(arr[num])
    l2.sort()
    i = 0
    for num in range(0,length):
        if num%2 == 0:
            arr[num] = l2[i]
            i += 1
        else:
            continue
    print(arr,end=' ')

length = int(input())
l1 = [int(x) for x in input().split()]
altsort(l1,length)

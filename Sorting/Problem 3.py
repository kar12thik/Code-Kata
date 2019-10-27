def firstalpha(l1):
    for item in l1:
        return item[0].lower()

length = int(input())
l1 = [input() for x in range(length)]
l1.sort(key=firstalpha)
print(*l1,sep='\n',end=' ')


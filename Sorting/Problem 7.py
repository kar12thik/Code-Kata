N, K = [int(x) for x in input().split()]
l1 = [int(x) for x in input().split()]

pos = 0

def search(arr, n):

    u = N - 1
    l = 0

    while l <= u:
        mid = (u+l) // 2

        if arr[mid] == n:
            globals()['pos'] = mid + 1
            return True
        else:
            if n > mid:
                l = mid + 1
            else:
                u = mid - 1
    return False

if search(l1,K) == True:
    print("yes")
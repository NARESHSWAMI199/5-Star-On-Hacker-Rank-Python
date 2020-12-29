


sk = list(map(int,input().split()))
arr = list(map(int,input().split()))

def hurdle(sk,arr):
    maximum = max(arr)
    if maximum > sk[1]:
        return maximum - sk[1]
    else :
        return 0
print(hurdle(sk,arr))
    
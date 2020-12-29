
arr1 = list(map(int ,input().rstrip().split()))
arr2 = list(map(int ,input().rstrip().split()))

def compareTriplets(a, b):
    cb = 0
    cs = 0

    for i in range(len(a)):
        if a[i] > b[i]  and a[i] != b[i]:
            cb +=1
        elif a[i] <  b[i] and a[i] != b[i]:
            cs +=1

    print(cb ,cs)
    
    
compareTriplets(arr1,arr2)
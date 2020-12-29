
nk = list(map(int,input().split()))
arr = list(map(int,input().split()))


def dsp(nk,arr):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(1,len(arr)):
            sum = arr[i] + arr[j]
            if sum % nk[1] == 0 and  i != j and i < j: 
                count +=1
    return count

print(dsp(nk,arr))
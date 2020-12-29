size = int(input())
arr = list(map(int,input().split()))

index = []

for i in range(1,size+1):
    for j in range(1,len(arr)+1):
        if i == arr[j-1]:
            index.append(j)
for i in  index:
    print(index[i-1])
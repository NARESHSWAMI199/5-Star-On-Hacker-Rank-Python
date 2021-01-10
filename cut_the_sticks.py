size = int(input())
arr = list(map(int,input().split()))
dict1 = { i : arr.count(i)  for i in sorted(arr) }
for key,value in dict1.items():
    print(size)
    size-=value
    


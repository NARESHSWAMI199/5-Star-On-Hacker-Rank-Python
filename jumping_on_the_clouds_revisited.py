n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
energy = 100



# while 1 in arr:
for i in range(0,n,k):
    if arr[i] == 1:
        energy = energy -1 -2
        arr[i] = 0
    else:
        energy = energy -1
    print(i)
print(energy)



# arr = [ 0,0,0,0,0]
# for i in arr:
#     if 1 in arr:
#         print("hello")
#     else:
#         print("task")
size = int(input())
arr = list(map(int,input().split()))

# jumped = (size-1)-arr.count('1')

def jumpingOnClouds(c):
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1: 
        return 1 + jumpingOnClouds(c[1:])
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])

print(jumpingOnClouds(arr))



# size = int(input())
# n = int(input())

# index  = 0
# g = []
# count =0
# for i in range(size):
#     value = list(map(int,input().split()))
#     g.append(value)    
#     for j in range(n):
#         if g[i][j]/g[index][j] == g[i][index]/g[index][index]:
#             count +=1
#         if index < n-1:
#             index +=1
# print(count)



# in other language if you find " 0 " in arr then incress 1 more time count
# int count = 0;
# for (int i = 0; i < n - 1; i++) {
#     if (c[i] == 0) i++;
#     count++;
# }
# System.out.println(count);






# test  for certification
# arr = [[4,8],[15,25],[25,50]]


# count = 0 

# i,j,k = 0,0,1

# while i != len(arr):
#     if arr[i][j] //arr[k][j] == arr[i][k]//arr[k][k]:
#         count +=1
#         print(arr[i][j] //arr[k][j] == arr[i][k]//arr[k][k])
#     else:
#         print(arr[i][j] //arr[k][j] == arr[i][k]//arr[k][k])

#     if k ==len(arr[0])-1:
#         k = 0
#     else:
#         k+=1
#     i +=1 
# print(count)




    
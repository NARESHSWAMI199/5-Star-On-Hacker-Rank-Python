# n,k,q=list(map(int,input().strip().split()))
# arr = list(map(int,input().strip().split()))

# new_arr = []

# k = k % n

# for i in range(k):
#         value = arr.pop()
#         new_arr.insert(0,value)
# new_arr += arr 

# for j in range(q):
#     print(new_arr[int(input())])




# this is working but only in python beacuse we using inbulid
# function 

# n,k,q=list(map(int,input().strip().split()))
# arr = list(map(int,input().strip().split()))

# for i in range(k):
#     value = arr.pop()
#     arr.insert(0,value)  # is in bulid function 
# for j in range(q):
#     print(arr[int(input())])



# logic of insert function

# n,k,q=list(map(int,input().strip().split()))
# arr = list(map(int,input().strip().split()))

# for i in range(q):
#     m = int(input())
#     print(arr[(n-(k%n)+m) % n])





# # this logic work in every laguage
# n,k,q=list(map(int,input().strip().split()))
# arr = list(map(int,input().strip().split()))

# k = k % n
# for _ in range(q):
#     index = int(input())
#     if index - k >= 0:
#         print(arr[index - k])
#         # print("i am working when index : ",index-k)
#     else:
#         # if index is nagtive then again add the len of the arr
#         print(arr[index-k+ len(arr)])
#         # print( " index : " ,index-k + len(arr) )


    

# 51 51 1
# 39356 87674 16667 54260 43958 70429 53682 6169 87496 66190 90286 4912 44792 65142 36183 43856 77633 38902 1407 88185 80399 72940 97555 23941 96271 49288 27021 32032 75662 69161 33581 15017 56835 66599 69277 17144 37027 39310 23312 24523 5499 13597 45786 66642 95090 98320 26849 72722 37221 28255 60906



n,k,q=list(map(int,input().strip().split()))
arr = list(map(int,input().strip().split()))
k = k%n
for _ in range(q):
    index = int(input())
    print(arr[index - k])
 

 # here don't need if else condition beacuse the python support 
 # nagative index for example arr[-1]
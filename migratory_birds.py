
# work for any input 
# size = input()
# arr = input().split()

# def max_migratory(arr):
#     visited = ''
#     dictnary = {}
#     for i in arr:
#         visited += i    
#         if i in visited:
#             dictnary.update({ i : visited.count(i)})
#     migratory = max(items for key, items in dictnary.items())
#     return min(key if migratory == value else 'naresh' for key,value in dictnary.items())
# print(max_migratory(arr))


# just work for 1 to 5 
# copied code 
input()
count = [0]*6
for i in map(int,input().strip().split()):
    count[i] += 1
    print(count)
print(count.index(max(count)))
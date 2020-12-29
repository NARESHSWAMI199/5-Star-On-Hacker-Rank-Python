# this code perfectlly count the mount
# size = input()
# arr = list(input())

# def count_vellay(arr):
#     answer = 0
#     count = 0
#     index = 0
#     for i in arr:
#         if i == "U":
#             count +=1
#         elif i == "D" :
#             count -=1
#         if count <= 0 and i =="U" and arr[index+1] =="D":
#             answer +=1
#         if index < (len(arr)-2):
#             index +=1
#     return answer

# print(count_vellay(arr))



size = input()
arr = list(input())


def count_vellay(arr):
    answer = 0
    count = 0
    for i in arr:
        if i == "U":
            count +=1
        elif i == "D" :
            count -=1
        if (count == 0 and i == "U"):
            answer+=1
    return answer


print(count_vellay(arr))
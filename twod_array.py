

list1 = []

for i in range(6):
    items2 = list(map(int,input().split()))
    list1.append(items2)
# def draw(list1):    
#     total = 0
#     ind = 3
#     for items in range(len(list1)):
#         for i in range(ind):
#             if (items == 1 and i==0) or (items ==1 and i==2):
#                 continue
#             total += list1[items][i]
#         if ind < 6:
#             ind +=1

#     print(total)

total = []
index = 3
for i in range(4):
    # draw(list1[i:index])
    items = list1[i:index]
    # print(items)
    list2 =[]
    for i in items:
        list2 +=i 
    print(sum(list2))

    
    if index < 6:
            index +=1

print(total)

size = int(input())
arr = []
for i in range(0,size):
    arr.append(list(input()))

index = 0
list2 = []
for i in range(len(arr)):
    list1 = arr[i]
    for j in range(i,(len(arr))):
        if list1[i] > list1[j] and list1[0] != "9":
            print(list1[i],list1[j])
            list1[i] = "X"
    for i in arr[i]:
        print(i,end='')
    print()



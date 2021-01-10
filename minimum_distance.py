size = input()
arr = list(map(int,input().split()))
def find_min(arr):
    dict1 = { i : arr.count(i) for i in arr}
    maximum = [value for key,value in dict1.items() if value > 1 ]
    values = [key  for key,value in dict1.items() if value in maximum]
    indexes = [i  for i in range((len(arr))) if arr[i] in list(sorted(values))]
    if values:
        ans = []
        for i in indexes:
            for j in indexes:
                if arr[i]==arr[j]:
                    if j-i > 0 and j > i:
                        ans.append(j-i)
        return(min(ans))
    else:
        return -1
print(find_min(arr))



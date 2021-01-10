
size = input()
arr = list(input().split())

def all_are_same(arr):
    dict1 = { x:arr.count(x) for x in sorted(arr)}
    maximum = max([value for key ,value in dict1.items()])
    return(len(arr)-maximum)
print(all_are_same(arr))
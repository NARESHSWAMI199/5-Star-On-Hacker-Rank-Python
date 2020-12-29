size = input()
arr = list(map(int,input().split()))
def sbm(arr):
    visited = []
    dictnary = {}
    answer = []
    for i in arr:
        visited.append(i)
        dictnary.update({ i : visited.count(i) if i in visited  else None})
    for key,value in dictnary.items():
        if value % 2 ==0:
            answer.append(value /2)
        elif value > 1:
            answer.append((value-1)/2)
    return int(sum(answer))
print(sbm(arr))
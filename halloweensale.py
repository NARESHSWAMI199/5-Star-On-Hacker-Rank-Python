p,d,m,s = list(map(int,input().split()))
list1 = []
while p > m:
    list1.append(p)
    p = p-d
list1 +=[m]*(s//m)
total = 0
ans = 0
for i in range(len(list1)):
    if total <= s:
        total+=list1[i]
        if total <= s:
            ans = i+1
print(ans)
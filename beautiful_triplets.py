s,d = list(map(int,input().split()))
arr = list(map(int,input().split()))
main = []
for i in arr:
    values = [i,(i+d),(i+d+d)]
    if (i) in arr and (i+d) in arr and(i+d+d) in arr:
        main.append(values)
print(len(main))



# for i in range(n):
#     if c[i]+d in c and c[i]+2*d in c:
#         gc+=1
# print (gc)
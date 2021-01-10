import sys
q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    parent = []
    for i in range(n):
       arr = [int(x) for x in input().strip().split(' ')]
       parent.append(arr)
    sv=[]
    sh=[]
    for i in range(n):
        sv.append(0)
        sh.append(sum(parent[i]))
        for j in range(n):
            sv[i]+=parent[j][i]
    sv.sort()
    sh.sort()
    if sv==sh:
        print("Possible")
    else:
        print("Impossible")
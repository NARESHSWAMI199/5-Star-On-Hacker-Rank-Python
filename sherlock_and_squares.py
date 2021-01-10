q = int(input())
for _ in range(q):
    s,e = list(map(int,input().split()))
    count = 0
    x = 1
    while(x*x < s):
        x+=1
    while(x*x <= e):
        count+=1
        x+=1
    print(count)


    # 5*5 < =49
    # 6*6 <=  36
t = int(input())
for _ in range(t):
    query = input()
    count  = 0
    for i in query:
        if int(i) !=0 and int(query) % int(i) == 0:
            count +=1
    print(count)
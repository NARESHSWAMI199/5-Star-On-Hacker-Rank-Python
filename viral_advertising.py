
days = int(input())

count = 0
liked = 0
shared = 5
comulative = 0
while count != days:
    # print(shared)
    liked = int(shared/2)
    shared = liked*3
    comulative +=liked
    count +=1


print(comulative)
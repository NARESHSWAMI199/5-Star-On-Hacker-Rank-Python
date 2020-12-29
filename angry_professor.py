

size = int(input())


for i in range(size):
    timed = []
    late = []
    size_and_student = list(map(int,input().split()))
    students_arrive_time = list(map(int,input().split()))

    for item in students_arrive_time:
        if item <= 0:
            timed.append(item)
        else:
            late.append(item)
    if len(timed) >= size_and_student[1]:
        print("NO")
    else:
        print("YES")



    

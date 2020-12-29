size = int(input())
height = []
total = []
for i in range(size):
    height.append(int(input()))

def needed_arr():
    answer = []
    n = 0
    count = 0
    while count != max(height)+1:
        n +=1
        answer.append(n)
        n = n*2
        answer.append(n)
        count +=1
    return answer

print(needed_arr())

for i in height:
    print(needed_arr()[i])





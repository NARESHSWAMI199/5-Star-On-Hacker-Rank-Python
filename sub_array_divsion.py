size = input()
arr = list(map(int , input().split()))
dm  = list(map(int , input().split()))

def sad(arr,day,month):
    newmonth = month
    count = 0
    for i in range(len(arr)):
        new = []
        for j in range(i , newmonth):
            new.append(arr[j])
        if newmonth < len(arr):    
            newmonth +=1
        if sum(new) == day and len(new) == month:
            count+=1
    return count
   
print(sad(arr,dm[0],dm[1]))

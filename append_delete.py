value = input()
modified_value = input()
k  = int(input())
same_value = []
length = len(value) if len(value) < len(modified_value) else len(modified_value) 
l = len(value) + len(modified_value)
for i in range(length):
    if value[i] != modified_value[i]:
        break
    same_value.append(i)
i = len(same_value)
print(( "Yes" if l<= k+i*2 and l%2 == k%2 or l < k  else "No"))
print(l)


# logic here 

# we add the both strings length 
#  and check the  

# here i is the same value in both strings
# value + modified_value , k + i*2 

# so simple mean the k is opreation which perform on string  or we can say if you perform one more action for remove or you
# can't. then you have perform an action this must be add in your action 

# then k is may be extra  compare the  visible changes 

# so the login is 

# l <= k + i*2 or l < k

# we add one condition like 
# l%2 == k%2 or l < k 
# for this like question
# y 
# yu
# 2
# Yes 

# that's ansewer No but give yes beacuse we don't k == len(both)




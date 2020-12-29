# we find here the minimum value which devide the all elemen of list
# or gcd  -> greatest common divisor

def greatest_common_divisor(a,b):
    while b > 0:
        tmp = b
        b = a%b   
        a = tmp
    return a

def pass_element(list1):
    result = list1[0]
    for i in range(1,len(list1)):
        result = greatest_common_divisor(result,list1[i])
    return result


# here int is predifine function
list1 = list(map(int,input().rstrip().split()))

print(pass_element(list1))


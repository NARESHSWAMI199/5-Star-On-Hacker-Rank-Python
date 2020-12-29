
# lowest common multiple  or fector  we finding lcm
#  gcd  -> greatest common divisor 

# this will return a shortest value divide all element
def gcd (a,b):
    while a > 0:
        tmp = a
        a = b%a
        b = tmp
    return b


def pass_input_gcd (arr):
    result = arr[0]
    for i in range(1,(len(arr))):
        result =  gcd(result,arr[i])
    return result

def lcm1(a,b):
    return a*(b/gcd(a,b))

def pass_input (arr):
    result = arr[0]
    for i in range(1,(len(arr))):
        result =  lcm1(result,arr[i])
    return result



arr = list(map(int,input().split()))
print(pass_input(arr) , " and ", pass_input_gcd(arr))





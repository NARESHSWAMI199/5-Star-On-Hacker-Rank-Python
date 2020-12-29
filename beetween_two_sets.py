class BeetweenTwoSets:

    # or gcd  -> greatest common divisor
    # this simple return minimum wihich 
    # will divided with all if 
    # not divide then return 1
    def gcd1(self,a,b):
        while (b > 0):
            tmp = b
            b = a%b  #is remainder
            a = tmp
        return a

    
# this will return the last return of 
# gcd1 or the minimum value 
#  which can divide your input 
    def gcd2(self,arr_input):
        result = arr_input[0]
        for i in range(1,len(arr_input)):
            result = self.gcd1(result,arr_input[i])
        return result

    # # this is simle find the lcm  
    def lcm1(self,a,b):
        return int(a*(b/self.gcd1(a,b)))
        

    # # this send our iput in lcm1 one same as gcd2
    # # and return the last return of lcm1
    def lcm2(self,arr_input):
        result = arr_input[0]
        for i in range(1,len(arr_input)):
            result = self.lcm1(result,arr_input[i])
        return result



# this are our input method which getting from user
# mn = list(map(int,input().rstrip().split()))
arr1 =  list(map(int,input().rstrip().split()))
arr2 = list(map(int,input().rstrip().split()))



obj = BeetweenTwoSets()


l = obj.lcm2(arr1)
g = obj.gcd2(arr2)

print(l ,"and " ,g)


count = 0
i =g 
j =2 
while i<=g:
    if g%i ==0: 
        count +=1
    print('before ',i , j)
    i = l*j
    j+=1
    print('after ' , i , j)


print(count)



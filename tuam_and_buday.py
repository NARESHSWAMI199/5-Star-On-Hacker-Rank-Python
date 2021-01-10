size = int(input())
for i in range(size):
    b,w = list(map(int,input().split()))
    bc,wc,z = list(map(int,input().split()))
    if bc > wc+z:
        print( (b*(wc+z)) + (w*wc)) 
    elif wc > bc+z:
        print( (b*bc) + (w*(bc+z)))
    else:
        print( (bc*b) + (w*wc))

    




# you can try it 


# 5       
# 10 10  
# 1 1 1   
# 5 9    
# 2 3 4   
# 3 6    
# 9 1 1   
# 7 7     
# 4 2 1   
# 3 3     
# 1 9 2   
quries_size = int(input())
maxmum = 0



for i in range(quries_size):
    query = list(map(int,input().split()))
    if query[0] > query[2]:
        dist_of_a = query[0] - query[2]
    else :
        dist_of_a = query[2]- query[0]
    
    if query[1] > query[2]:
        dist_of_b = query[1] - query[2]
    else :
        dist_of_b = query[2]- query[1]
    
    if dist_of_a < dist_of_b:
        print("Cat A")
    elif dist_of_b < dist_of_a:
        print("Cat B")
    else : 
        print("Mouse C")

        
  


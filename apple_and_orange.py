
house_range = list(map(int,input().rstrip().split())) # s->t
apple_orange_dis = list(map(int,input().rstrip().split())) # a->b
apple_orange_num = list(map(int,input().rstrip().split())) # m n  

apples_throw_dis = list(map(int,input().rstrip().split())) 
orange_thorow_dis = list(map(int,input().rstrip().split())) 




def check_apple( hr,ab,aon,atd,otd):
    count_apple = 0
    count_orange = 0
    atd_sum  = [ab[0]+item  for item in atd]
    otd_sum = [ab[1]+item for item in otd]

    for item in atd_sum:
        if item == hr[0] or item==hr[1] or  item > hr[0] and item < hr[1]:
            count_apple +=1
        
    for item in otd_sum:
        if item == hr[0] or item==hr[1] or item > hr[0] and item < hr[1]:
            count_orange +=1
    
    print(count_apple)
    print(count_orange)

check_apple(house_range,apple_orange_dis,apple_orange_num,apples_throw_dis,orange_thorow_dis)
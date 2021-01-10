from itertools import combinations
n,k = map(int,input().split())
teams = [list(map(int,list(input()))) for i in range(n)]
print("combination : " ,list(combinations(teams,2)))
sums = [sum([x[0] or x[1] for x in list(zip(*i))]) for i in combinations(teams,2)]
print(max(sums),sums.count(max(sums)),sep='\n')



# for i in combinations(teams,2):
#     for x in list(zip(*i)):
#         print(x)


# for i in combinations(teams,2):
#     for x in list(zip(*i)):
#         print("how : ",  x[0] or x[1], end=' ')

# for i in combinations(teams,2):
#     for x in list(zip(*i)):
#         print()
#         print("here : ",x[0] , x[1], end=' ')

# for i in combinations(teams,2):
#     print( sum([ x[0] or x[1]  for x in list(zip(*i))]))



# arr = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

# for i in list(zip(*arr)):
#     print(sum([i[0] or i[1]]))



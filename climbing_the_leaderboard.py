size1 = input()
ranks = list(map(int,input().split()))
size2 = input()
players = list(map(int,input().split()))

















# new_rank = []
# for i in ranks:
#     if i not in new_rank:
#         new_rank.append(i)

# new_player = []
# for i in players:
#     if i not in new_player:
#         new_player.append(i)



# def find_rank(ranks,players):
#     answer = []
#     ranked = {}
#     for i in range(1,len(ranks)+1):
#         ranked.update({ i : ranks[i-1]})

#     for key,value in ranked.items():
#         for j in players:
#             if value <= j:
#                 answer.append(key)
#                 players.pop()
#     if len(players) > 0:
#         if players[0] < ranks[-1]:
#             answer.append(len(ranks)+1)

#     for i in reversed(answer):
#         print(i)

# find_rank(new_rank,new_player)
            

            
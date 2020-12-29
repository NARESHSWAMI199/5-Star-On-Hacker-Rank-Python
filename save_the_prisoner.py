
# # this right according logic but complexity is so heavy  working but good for a large input
# querys_num = int(input())

# def saving(querys_num):
#     for _ in range(querys_num):
#         m,n,s = list(map(int,input().split()))
#         prisoners = [x for x in range(1,m+1)]
#         # ans = 0
#         index = s
#         for i in range(n):
#             # print("the index going ",index)
#             ans = prisoners[index-1]
#             if index == len(prisoners)-1:
#                 # print("index : ",index)
#                 index %= m
#             elif index < len(prisoners):
#                 index +=1
#         print(ans)
#         # print(prisoners)

# saving(querys_num)
    





# this will in low complexcity

# T = int(input().strip()) # size of input
# for _ in range(T):
#     N,M,S = list(map(int, input().strip().split()))  # input  n = pepople , m= sweet , 2 seet
#     # print("s - 1 + m -1 : ",(S - 1 + M - 1))
#     # print("(s - 1 + m -1) % N : ",(S - 1 + M - 1) %  N)
#     print(((S - 1 + M - 1) % N) + 1)


    # The S-1 translates the prisoner id to an equivalent index (since % effectively deals with indexes like 0..N-1).
    # The M-1 handles the fact that the first prisoner to get a sweet is not counted when giving away sweets. 
    # Example, if you are giving away 1 sweet and you start at prisoner 37, it is 37 = (37 + 1 - 1) 
    # that should be warned. If you are giving away 2 sweets it is 38 = (37 + 2 - 1) that should be warned. 
    # And so on. The % N handles the wrapping around based on the index of the prisoners. And the + 1 brings us
    # back to dealing with prisoner ID's instead of indicies.




# S-1 कैदी आईडी का समकक्ष इंडेक्स में अनुवाद करता है (चूंकि% 0..N-1 जैसे इंडेक्स के साथ प्रभावी रूप से संबंधित है)। 
# M -1 इस तथ्य को संभालता है कि मिठाई पाने वाले पहले कैदी की गिनती मिठाई देते समय नहीं की जाती है। उदाहरण, यदि आप 1 मिठाई दे रहे हैं 
# और आप कैदी 37 पर शुरू करते हैं, तो यह 37 = (37 + 1 - 1) है जिसे चेतावनी दी जानी चाहिए। 
# यदि आप 2 मिठाई दे रहे हैं तो यह 38 = (37 + 2 - 1) है
# जिसे चेतावनी दी जानी चाहिए। और इसी तरह। % N कैदियों के सूचकांक के आधार पर चारों ओर की लपेट को संभालता है। 
# और + 1 हमें संकेत के बजाय कैदी आईडी से निपटने के लिए वापस लाता है


# the logic

#how many inputs or count query
input_size = int(input())

for i in range(input_size):
    prisoners,sweets,start_point = list(map(int,input().split()))
    # Start_point-1 कैदी आईडी का समकक्ष इंडेक्स में अनुवाद करता है (चूंकि% 0..N-1 जैसे इंडेक्स के साथ प्रभावी रूप से संबंधित है)। 
    print(((start_point-1 + sweets-1) % prisoners) + 1)
    # । उदाहरण, यदि आप 1 मिठाई दे रहे हैं 
    # और आप कैदी 37 पर शुरू करते हैं, तो यह 37 = (37 + 1 - 1) है
    # जिसे चेतावनी दी जानी चाहिए। यदि आप 2 मिठाई दे रहे हैं तो यह 38 = (37 + 2 - 1) है

# adding stop_pont -1 + sweet-1  beacude we must include the leaved user



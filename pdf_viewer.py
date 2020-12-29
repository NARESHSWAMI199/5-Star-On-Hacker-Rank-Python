

user_arr = list(map(int,input().split()))
word = list(input().lower())
arr = ['a','b','c','d','e','f','g','h','i','j','k',
        'l','m','n','o','p','q','r','s','t','u','v',
        'w','x','y','z']

def find_area(arr,user_arr,word):
    index = 0
    word_index = []
    for item in arr:
        for i in word:
            if item == i:
                word_index.append(arr.index(item))
    ans = []
    for i in word_index:
        ans.append(user_arr[i])
    return max(ans)*len(word)
print(find_area(arr,user_arr,word))
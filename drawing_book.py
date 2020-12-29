total_pages  = int(input())
want_page = int(input())

def db(total_pages,want_page):
    front = [i for i in range(0,total_pages+1,2)]
    end = list(reversed(front))
    ans = []
    [ans.append(front.index(front[i])) if front[i] == want_page or front[i]+1  == want_page  else 0 for i in range(len(front))]
    [ans.append(end.index(end[i])) if end[i] == want_page or end[i]+1  == want_page else 0 for i in range(len(end))]
    print(min(ans))
db(total_pages,want_page)
        

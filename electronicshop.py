budget = list(map(int,input().split()))
keybords = list(map(int,input().split()))
drives = list(map(int,input().split()))


def can_purchase(budget,keybords,drives):
    keybords = sorted(keybords)
    drives = sorted(drives)
    max = -1
    for i in range(len(keybords)):
        for j in range(len(drives)):
            if (keybords[i]+drives[j] > budget):
                break
            if keybords[i]+drives[j] > max:
                max = keybords[i]+drives[j]
                print(keybords[i] , " this  ", drives[j])
                print(max)
    return max
print(can_purchase(budget[0],keybords,drives))


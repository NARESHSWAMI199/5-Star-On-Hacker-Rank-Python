

def genrateSquare():
    n = 3
    magicSquare = [[0 for x in range(n)] for y in range(n)]
    # insert first value on index
    i = int(n/2)
    j = n-1

    num = 1
    while num <= (n*n):

        if i ==-1 and j == n:
            i = 0
            j = n - 2
        else :

            if j == n:
                j = 0

            if i < 0:
                i = n - 1
        # if value is occupied on the same index then 
        if magicSquare[i][j]:
            i = i + 1
            j = j - 2
            continue
        else:   
            magicSquare[i][j] = num
            num = num + 1  

        i = i - 1
        j = j + 1

    
    return magicSquare

func = genrateSquare()


arr = [
    list(map(int , input().split())),
    list(map(int , input().split())),
    list(map(int , input().split()))
]


def createMagicSquare(arr , pre_magic ):
    for i in  reversed(range(3)):
        print(pre_magic[i])

    print ('--------------------------------------------')
    for i in range(3):
        print(pre_magic[i])



createMagicSquare(arr,func)

    
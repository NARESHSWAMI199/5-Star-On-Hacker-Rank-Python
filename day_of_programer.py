year = int(input())
leap_not = [1700, 1800, 1900, 2000, 2400]
def dop(year):
    if year == 1918:
        print(f"26.09.{year}")
    elif year in leap_not:
        print(f"12.09.{year}")
    elif  year % 4 != 0:
        print(f"13.09.{year}")
    elif year % 4 != 0 or year % 100 == 0:
        print(f"13.09.{year}")
    elif  year % 400 ==0:
        print(f"13.09.{year}")
    else:  
        print(f"12.09.{year}")
dop(year)






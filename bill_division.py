size_index  = list(map(int,input().split()))
bill = list(map(int,input().split()))
total_charge = int(input())


def bill_divi(index, bill,total):
    bill.pop(index)
    value = 0
    for i in bill:
        value +=i
    value = value/2

    if total == value:
        return 'Bon Appetit'
    else:
        total -= value
        return int(total)

print(bill_divi(size_index[1],bill,total_charge))
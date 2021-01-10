
n, k = list(map(int,input().strip().split()))
numbers = list(map(int,input().strip().split()))

counts = [0] * k
for number in numbers:
    counts[number % k] += 1
print(counts)

count = min(counts[0], 1)
for i in range(1, k//2+1):
    if i != k - i:
        count += max(counts[i], counts[k-i])
if k % 2 == 0: 
    count += 1

print (count)




# n,k = list(map(int,input().strip().split()))
# numbers = list(map(int,input().strip().split()))

# for i in range(len(numbers)):
#     for j in range( i+1,len(numbers)):
#         print((numbers[i] + numbers[j])%k)


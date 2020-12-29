x1v1x2v2 = list(map(int,input().rstrip().split()))

v1 = x1v1x2v2[1]
v2 = x1v1x2v2[3]

x1 = x1v1x2v2[0]
x2 = x1v1x2v2[2]

print("YES" if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0 else "NO")

# or you can say both are right


print("YES" if x2 > x1 and v1 > v2 and (x2 - x1) % (v2 - v1) == 0 else "NO")

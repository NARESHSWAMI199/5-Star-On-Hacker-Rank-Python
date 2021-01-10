rd,rm,ry = list(map(int,input().split()))
gd,gm,gy = list(map(int,input().split()))

fine = 0
if rd <= gd and rm <=gm and ry <= gy:
    fine = 0
elif rd > gd and rm == gm and  ry == gy:
    fine = 15 * (rd-gd) 
elif rm > gm and ry == gy:
    fine = 500 * (rm-gm)
elif ry > gy:
    fine = 10000
print(fine)
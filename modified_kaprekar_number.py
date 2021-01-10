start_point = int(input())
end_point  = int(input())

string = ''
if start_point == 0  or start_point == 1:
	print(1 ,end=' ')
for x in range(start_point,end_point+1):
	square = str(x*x)
	length = len(square) // 2
	if len(square) == 1:
		continue
	else:
		if int(square[0:length]) + int(square[length : ])  == x:
			print(x ,end=' ')
			string+=str(x)
if len(string)==0:
	print('INVALID RANGE')



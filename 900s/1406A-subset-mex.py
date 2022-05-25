getLine = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
	n = int(input())
	a = getLine()
	d = {}
	d = {i : 0 for i in range(101)}
	
	for ai in a:
		d[ai] += 1
	
	for k,v in sorted(d.items()):
		if v == 0:
			A = k
			break
	for k,v in sorted(d.items()):
		if v <= 1:
			B = k
			break		
	print(A+B)
	
	
	


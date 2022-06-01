t = int(input())
getLine = lambda : map(int, input().split())

for _ in range(t):
	n = int(input())
	xs = list(getLine())
	if (xs[-1]-xs[0]) <= n+1:
		print('YES')
	else:
		print('NO')
	

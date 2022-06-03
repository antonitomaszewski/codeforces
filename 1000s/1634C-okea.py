getLine = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
	n, k = getLine()
	if n % 2 == 1:
		if k == 1:
			print('YES')
			for i in range(1,n+1):
				print(i)
		else:
			print('NO')
	else:
		print('YES')
		for i in range(1, n+1):
			for j in range(k):
				print(i + j*n, end=' ')
			print()

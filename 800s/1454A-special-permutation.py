getLine = lambda : map(int, input().split())

t = int(input())
for _ in range(t):
	n = int(input())
	xs = [n] + [i for i in range(1,n)]
	for i in range(n):
		print(xs[i], end=' ')

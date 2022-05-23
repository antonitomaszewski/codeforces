getLine = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
	n = int(input())
	a = sorted(getLine(), reverse=True)
	if n == 2:
		print(0)
	else:
		print(min(a[0]-1, a[1]-1, n-2))


getLine = lambda : map(int, input().split())
t = int(input())
for _ in range(t):
	a,b = getLine()
	print(max(2*min(a,b), max(a,b))**2)

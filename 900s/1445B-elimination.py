getLine = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
	a,b,c,d = getLine()
	print(max(a+b, c+d))

getLine = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
	n, r, b = getLine()
	base = r // (b+1)
	rest = r % (b+1)
	print(('R' * (base+1) + 'B') * rest + ('R' * base + 'B') * (b-rest) + 'R' * base)
	

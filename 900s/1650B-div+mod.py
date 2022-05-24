getLine = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
	l, r, a = getLine()
	kandydat = r // a * a - 1
	if l <= kandydat:
		print(max(kandydat // a + kandydat % a, r // a + r % a))
	else:
		print(r // a + r % a)

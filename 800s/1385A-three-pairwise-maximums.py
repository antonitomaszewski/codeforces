getLine = lambda : map(int, input().split())

t = int(input())
for _ in range(t):
	a,b,c = sorted(getLine())
	if b < c:
		print("NO")
	elif a == b == c:
		print(f"YES\n{a} {b} {c}")
	else:
		print(f"YES\n{1} {a} {b}")

t = int(input())

a = 2020
b = 2021
d = {0 : 1}

def f(n):
	if n in d:
		return d[n]
	if n < a:
		d[n] = 0
		return d[n]
	l = f(n-a)
	r = f(n-b)
	d[n] = l or r
	return d[n]
	
for _ in range(t):
	n = int(input())
	print(['NO', 'YES'][f(n)])


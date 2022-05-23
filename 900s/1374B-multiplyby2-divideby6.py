t = int(input())
for _ in range(t):
	n = int(input())
	k = 0
	while n % 3 == 0:
		k += 1
		n //= 3
	l = 0
	while n % 2 == 0:
		l += 1
		n //= 2
#	print (k, l)
	if n == 1 and k >= l:
		print(k + k-l)
	else:
		print(-1)

t = int(input())
for _ in range(t):
	n = int(input())

	c4, r4, c6, r6 = n//4, n%4, n//6, n%6
	max = c4
	min = c6 + (r6 != 0)
	if n % 2 != 0 or n < 4:
		print(-1)
	else:
		print(min, max)
	
	
	

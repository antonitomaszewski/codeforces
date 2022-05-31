import numpy as np

getLine = lambda : map(int, input().split())
t = int(input())


for _ in range(t):
	n, m = getLine()
	xs = []
	coordinates = lambda i,j : (j-i, m-1-j - i)
	for _ in range(n):
		x = list(getLine())
		xs.append(x)
	A = np.array(xs)
	antiA = np.fliplr(A)
	r = list(range(m)) + list(range(-n+1,0))
	Diags = {i : A.diagonal(i) for i in r}
	DiagsSums = {k : v.sum() for k,v in Diags.items()}
	AntiDiags = {i : antiA.diagonal(i) for i in r}
	AntiDiagsSums = {k : v.sum() for k,v in AntiDiags.items()}
#	print(Diags)
#	print(AntiDiags)
	vs = [[0 for _ in range(m)] for _ in range(n)]
	sums = [[0 for _ in range(m)] for _ in range(n)]
	maxi = 0
	for i in range(n):
		for j in range(m):
#			print(f'i={i}, j={j} : {coordinates(i,j)}')
			coors = coordinates(i,j)
			vs[i][j] = DiagsSums[coors[0]], AntiDiagsSums[coors[1]]
			sums[i][j] = DiagsSums[coors[0]] + AntiDiagsSums[coors[1]] - xs[i][j]
			maxi = max(maxi, sums[i][j])
			
#	print(vs)
	print(maxi)
			
	
	

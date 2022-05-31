getLine = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
	n, m = getLine()
	xs = []
	for _ in range(n):
		x = list(getLine())
		xs.append(x)
	
	indeksyDiag = [i for i in range(-n+1, m)]
	macierzDiag = [indeksyDiag[i:i+m] for i in range(n-1, -1, -1)]
	macierzAntiDiag = [indeksyDiag[i:i+m] for i in range(0, n)]
	Diagonale = {i : [] for i in indeksyDiag}
	AntiDiagonale = {i : [] for i in indeksyDiag}

	for i in range(n):
		for j in range(m):
			Diag = macierzDiag[i][j]
			antiDiag = macierzAntiDiag[i][j]
			Diagonale[Diag].append(xs[i][j])
			AntiDiagonale[antiDiag].append(xs[i][j])

	DiagonaleSumy = {k : sum(v) for k,v in Diagonale.items()}
	AntiDiagonaleSumy = {k : sum(v) for k,v in AntiDiagonale.items()}
#	print(DiagonaleSumy)
#	print(AntiDiagonaleSumy)
	
	maxi = 0
	for i in range(n):
		for j in range(m):
			indeksDiag = macierzDiag[i][j]
			indeksAntiDiag = macierzAntiDiag[i][j]
			value = (DiagonaleSumy[indeksDiag]
			+ AntiDiagonaleSumy[indeksAntiDiag]
			- xs[i][j]
			)
			maxi = max(maxi, value)
	print(maxi)	

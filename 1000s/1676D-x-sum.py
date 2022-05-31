getLine = lambda : map(int, input().split())


def diagMatrix(M):
	Top = [[j-i for j in range(M)] for i in range(M)]
	Bottom = [[j-M+1+i for j in range(M)] for i in range(M)]
	return Top, Bottom

def TopDiagonalCoordinates(j, M):
	return list(filter(lambda x: M > x[1] >= 0, ((i, j+i) for i in range(M))))
def BottomDiagonalCoordinates(j, M):
	return list(filter(lambda x: M > x[1] >= 0, ((i, j+M-1-i) for i in range(M))))
	
def CoordinatesToValues(coordinates, Matrix):
	return [Matrix[i][j] for i,j in coordinates]
def coordinateToDiagCoordinates(i,j, M):
	return j-i, j-(M-1-i)
	
t = int(input())
for _ in range(t):
# wczytanie wartości i dodanie wypełnienia
	n, m = getLine()
	M = max(n,m)
	xs = []
	for _ in range(n):
		x = list(getLine()) + [0] * (M-m)
		xs.append(x)
	xs.append((M-n) * [0 for _ in range(M)])
	xs = xs[:M]
	
	TopDiagonalSums = {j : sum(CoordinatesToValues(TopDiagonalCoordinates(j, M), xs)) for j in range(-M+1, M)}
	BottomDiagonalSums = {j : sum(CoordinatesToValues(BottomDiagonalCoordinates(j, M), xs)) for j in range(-M+1, M)}
	
	DiagMatrixTop, DiagMatrixBottom = diagMatrix(M)
	res = 0
	for i in range(M):
		for j in range(M):
			diagCoordinateTop = DiagMatrixTop[i][j]
			diagCoordinateBottom = DiagMatrixBottom[i][j]
			bishopValue = (TopDiagonalSums[diagCoordinateTop]
			+ BottomDiagonalSums[diagCoordinateBottom]
			- xs[i][j])
			res = max(res, bishopValue)
	print(res)
	
	
"""
t = int(input())

for _ in range(t):
	n, m = getLine()
	M = max(n,m)
	xs = []
	for _ in range(n):
		x = list(getLine()) + [0] * (M-m)
		xs.append(x)
	xs.append((M-n) * [0 for _ in range(M)])
	xs = xs[:M]
	rightDiag = {(i, j) : 
		sum(xs[k][l] for k,l in zip(range(i, M), range(j,M)))
		for i, j in ([(0, j) for j in range(M)]
			+ [(i, 0) for i in range(1, M)])
	}
	leftDiag = {(i, j) :
		sum(xs[k][l] for k,l in zip(range(i,-1,-1), range(j,M)))
		for i, j in (
		[(i, 0) for i in range(M)]
		+ [(M-1, j) for j in range(1,M)]
		)
	
	}
	ys = [[0 for _ in range(M)] for _ in range(M)]
	for i in range(M):
		for j in range(M):
			diagSum = (rightDiag[(i-min(i,j),j-min(i,j))]
				+ leftDiag[(min(i+j, M-1), max(i+j-M+1,0))]
				- xs[i][j])
			ys[i][j] = diagSum
	print(max(max(y) for y in ys))
	
"""
	
	

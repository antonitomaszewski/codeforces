getLine = lambda : map(int, input().split())

n = int(input())
B = [0] + list(getLine())
X = [0 for _ in range(n+1)]
A = [0 for _ in range(n+1)]
prevMax = 0

for i in range(1, n+1):
	X[i] = prevMax
	A[i] = B[i]+X[i]
	prevMax = max(prevMax, A[i])
	
print(' '.join(map(str, A[1:])))


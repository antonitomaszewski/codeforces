numberOfTests = int(input())
for _ in range(numberOfTests):
	n, m = map(int, input().split())
	print(["NO", "YES"][n % m == 0])

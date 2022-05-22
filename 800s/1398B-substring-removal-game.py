numberOfTests = int(input())
for _ in range(numberOfTests):
	s = input()
	ones = s.split('0')
	movesByBest = sorted(ones, key=len, reverse=True)
	AlicesMoves = movesByBest[::2]
	AlicesResult = len(''.join(AlicesMoves))
	print(AlicesResult)

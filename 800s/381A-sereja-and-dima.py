getLine = lambda : map(int, input().split())

n = int(input())
cards = list(getLine())
sereja, dima = 0, 0
lIndex, rIndex = 0, n-1
for move in range(n):
	if cards[lIndex] < cards[rIndex]:
		if move % 2 == 0:
			sereja += cards[rIndex]
		else:
			dima += cards[rIndex]
		rIndex -= 1
	else:
		if move % 2 == 0:
			sereja += cards[lIndex]
		else:
			dima += cards[lIndex]
		lIndex += 1
#	print(f'sereja={sereja}, dima={dima}')
print(sereja, dima)

getLine = lambda : map(int, input().split())
t = int(input())
for _ in range(t):
	b, p, f = getLine()
	h, c = getLine()
	if h < c:
		p, f = f, p
		h, c = c, h
	noH = min(b//2, p)
	hProfit = h * noH
	noC = min((b - 2*noH)//2, f)
	cProfit = c * noC
	print(hProfit + cProfit)
	

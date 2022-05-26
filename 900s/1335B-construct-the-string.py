import string
import itertools

string.ascii_lowercase
itertools.repeat

getLine = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
	n, a, b = getLine()
	baseString = string.ascii_lowercase[:b]
	xs = itertools.repeat(baseString, n//b + 1)
	resultString = ''.join(xs)[:n]
	print(resultString)

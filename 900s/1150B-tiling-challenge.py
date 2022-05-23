def check(xss, i, j):
	if xss[i][j] != '.':
		return 0
	if xss[i+1][j-1] != '.':
		return 0
	if xss[i+1][j] != '.':
		return 0
	if xss[i+1][j+1] != '.':
		return 0
	if xss[i+2][j] != '.':
		return 0
	xss[i][j] = '#'
	xss[i+1][j-1] = '#'
	xss[i+1][j] = '#'
	xss[i+1][j+1] = '#'
	xss[i+2][j] = '#'
	return 1

def main():
	n = int(input())
	xss = []
	for _ in range(n):
		line = list('##' + input() + '##')
		xss.append(line)
	xss += 2*[list((n+4)*'#')]
	for i in range(0,n):
		for j in range(2,n+2):
#			print(f'i={i}, j={j}\n {xss[i][j]} \n{xss[i+1][j-1]}{xss[i+1][j]}{xss[i+1][j+1]}\n {xss[i+2][j]} ')
			if xss[i][j] == '#':
				pass
			elif check(xss, i, j):
				pass
			else:
				print(f'NO')
#				print(xss)
				return
	print('YES')
main()


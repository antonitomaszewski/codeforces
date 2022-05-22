x = input().split('.')
if x[0][-1] == '9':
	print("GOTO Vasilisa.")
elif x[1][0] >= '5':
	print(f'{x[0][:-1]}{int(x[0][-1])+1}')
else:
	print(x[0])

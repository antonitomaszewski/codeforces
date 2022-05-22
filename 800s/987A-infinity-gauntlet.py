gems = {'purple' : 'power', 'green' : 'time', 'blue':'space', 'orange':'soul', 'red':'reality', 'yellow':'mind'}
n = int(input())
for _ in range(n):
	del gems[input()]
print(len(gems))
for gem in gems.values():
	print(gem.title())

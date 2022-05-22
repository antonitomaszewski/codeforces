vowels = ['a', 'e', 'i', 'o', 'u']
countVowels = lambda : len(list(filter(lambda c : c in vowels, input())))
print(["NO", "YES"][countVowels()==5 and countVowels()==7 and countVowels()==5])


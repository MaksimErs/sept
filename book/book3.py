volowes = ['a', 'e', 'i', 'o', 'u']
word = input('Ввди слово для поиска гласных: ')
found = []
for letter in word:
    if letter in volowes:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
v = set('aeiou')
w = 'hello'
u = v.union(set(w))
d = v.difference(set(w))
i = v.intersection(set(w))
print(u, d, i)


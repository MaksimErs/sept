volowes = ['a', 'e', 'i', 'o', 'u']
word = input('Ввди слово для поиска гласных: ')
found = {}
for letter in word:
    if letter in volowes:
        found.setdefault(letter,0)
        found[letter] +=1
a = {k:v for k,v in sorted(found.items())}
d = [(k,v) for (k,v) in sorted(found.items())]
print(a)
print(d)
print(found)


'''if letter not in found:
            found.append(letter)
print(found)'''
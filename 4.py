p = [1, 0, 0, 1, 1]
f = [i for i in p if i == p[1] ]
print(f)
v = [i for i in p if i == 1]
print(v)
if len(f) < len(v): print(len(f), 'монет перевернем')
else: print(len(v), 'монет перевернем')
# создание из одного списка двух с условием, и сравнение их длин
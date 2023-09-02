set_1 = set()
set_2 = set()

a = [2,3,6,6,7]
k = set(a)
for i in k:
    set_1.add(i)
b = [5,4,6,7]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
    
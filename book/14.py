set_1 = set()
set_2 = set()

a = [2,3,6,6,7]
k = set(a)
print(k)
b = [5,4,6,7]
k1 = set(b)
print(k1)
lok = k & k1
print(lok)
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
    
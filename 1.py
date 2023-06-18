import datetime
j = datetime.time()
print(j)
x = 42
if isinstance(x, int):
    print("целое")
n = [1,2,3]
l = ['f','g','h']
p = zip(n,l)
for pa in p:
    print(pa)
fruits = ['apple','banane','orange' ]
for index, fruit in enumerate(fruits):
    print(index, fruit)
            
    
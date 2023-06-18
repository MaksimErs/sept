import random
n = int(input())
f = []
for _ in range(n): f.append(random.randint(0,5))
print(f)
x = int(input())
p = [i for i in f if i == x]
print(p)
print(len(p))
# сколько раз встречается число 5

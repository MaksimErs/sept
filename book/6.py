import random
f = []
for _ in range(10): f.append(random.randint(0,51))
print(f)
p = [i for i in range(10)]
print(p)
g = f + p
print(g)
# создание рандомного списка, создание списка от 1 до 10, объединение списков 
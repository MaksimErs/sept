s = str(input())
l = list(s)
print(l)
p = ['а', 'в']
p0 = [i for i in l if i == p[0]]
p1 = [i for i in l if i == p[1]]
V = ['д', 'у']
v0 = [i for i in l if i == p[0]]
v1 = [i for i in l if i == p[1]] 
f = len(p0) + len(p1) + len(v0) *2 + len(v1) *2
print(f)
# принцип подсчета очков в задаче 20 таков, можно делать так но болшой объем, как это зациклить?
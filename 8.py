import random
n = int(input())
f = []
for _ in range(n): f.append(random.randint(0,7))
print(f)
x = 5
p = [i for i in f if i >= 0]
print(p)
p.append(x)
p.sort()
p.reverse()
r = p.index(x)
s = len(p)
print(p)
print(r)
print(s)
if r == 0: 
    print(p[1]) 
else:
    if r == s - 1: 
        print(p[s - 2])
    else:
        k = p[r - 1]
        u = p[r + 1]
        if k - x > x-u: 
            print(u)
        else: 
             print(k) 
        
         

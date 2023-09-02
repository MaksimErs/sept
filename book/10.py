import random
n = int(input())
f = []
for _ in range(n): f.append(random.randint(-7,7))
print(f)
x = int(input())
if x >= 0 : 
    p = [i for i in f if i >= 0]
    print(p)
    if len(p) == 0:
        f.sort()
        print(f[len(f) - 1])
    else:
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
else:
    p = [i * -1 for i in f if i <= 0]
    print(p)
    if len(p) == 0:
        f.sort()
        print(f[0])
    else:
        p.append(-x)
        p.sort()
        p.reverse()
        r = p.index(-x)
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
                if k - -x > -x - u: 
                    print('минус',u)
                else: 
                    print('минус',k) 
  # находим близкий к заданному числу элемент          
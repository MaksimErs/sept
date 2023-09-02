'''n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i+=1'''
import copy
x = {0:23,1:45}
y = copy.deepcopy(x)
print(y)
word = 'as dor sdot sdot as as as'
df = {}
for t in word.split():
    df.setdefault(t,0)
    df[t]+=1
print(df)
from collections import Counter
s = Counter('as dor sdot sdot as as as'.split())
print(dict(s))


    
     
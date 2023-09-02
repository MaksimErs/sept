#f = 'dsae'
#print(f.count('d','e'))
def s(d):
    a= d
    def sd(q):
        print(a*q)
    return sd


e = s(5)
e(4)
e(2)



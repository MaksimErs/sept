def dgf():
    m = 123456
    m = str(m)
    print(str(m))
    print(type(m))
    k = list(m)
    print(k)
    k[1] = 'c'
    c = ''.join(k)
    print(c)
    l = '1,c,2,3'
    d = l.split(',')
    print(d)
    vars()
    g = vars()
    return g
print (dgf())



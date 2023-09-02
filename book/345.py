def sdf(func):
    def ddf():
        d = float(input('введи число:'))
        a = float(input('введи число:'))
        c = func(d, a)
        return c
    return ddf
@sdf
def asd(x, y):
    f = x*y
    print(f)
asd()

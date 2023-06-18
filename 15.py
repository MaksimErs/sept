def progres(q, w, r):
    l = [q + (n -1)*r for n in range(1, (w + 1))]
    return l
    
a = int(input('введи первое число'))
s = int(input('введи количество элементов'))
d = int(input('введи разность'))
print(progres(a, s, d))

# задача 30 заполните массив элементами арифметич прогрессии
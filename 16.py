def index(lst, min_a, max_b):
    l = [x for x in range(len(lst)) if  min_a <= d[x] <= max_b ]
    return l
    

d = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7 ]
a = 7
b = 10
print(index(d, a, b))

# задача 32 определите индексы  элементов массива значения которых в диапазоне
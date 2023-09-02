# задача 36 вычисление элемента по номеру строки и столбца(вариант)
def print_oper(op,x,y):
    print(op(x,y))
    
def fors(rows,columns):
    d = []
    for a in range(1, rows + 1):
        for b in range(1,columns + 1):
            c = a * b
            d.append(c)
    return d
        
print_oper(fors,6,6)


        
        
        
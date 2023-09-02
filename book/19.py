# задача 34 вариант решения Вини-пух(па папа па)
data = input().split()
print(data)

def funk(D):
    x = 0
    while x < (len(D) - 1):
        if list(D[x]).count('а') != list(D[x+1]).count('а'):
            print('такта нет')
            break
        x = x +1
    else:
        print(' цикл пройден такт есть')    
   
funk(data)     
list = ['pop','dod','pop']
list1 = []
list2 = []
for _ in list:
    if _ == 'pop':
        list1.append(1)
        list2.append(0)
    else:
         list1.append(0)
         list2.append(1)
d = [x for x in zip(list1 , list2)]            
print(d)
        
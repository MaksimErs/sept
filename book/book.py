from datetime import datetime
import time
import random
for x in range(5):
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd")
    else:
        print("not an odd minute")
    time.sleep(random.randint(1,60))


'''from os import getcwd  # функция при вызове возвращает текущий рабочий каталог
where_am = getcwd()
print(where_am)
import sys
print(sys.platform)
print(sys.version)'''
'''import os
print(os.environ)'''
'''import datetime
print(datetime.date.isoformat(datetime.date.today()))
import time
print(time.strftime("%I:%M"))'''

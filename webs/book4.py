

"""def sds(func):
 def qwe():
    ar = "ea" #input('введи какие гласные ищем: ')
    wo = "es,aas" #input('Ввди слова  для поиска гласных через запятую: ')
    if ',' not in wo:
        wot = wo + ','
        wos = wot.split(',')
    else:
        wos = wo.split(',')
    if wos[len(wos) - 1] == '':
        wos = wos[0:len(wos) - 1]
    if ar == '':
        ar = 'u'
    d = func(ar, wo)
    return d
 return qwe

@sds"""
def search4vowels(arg, word):
    """ищем гласные в указанном слове"""

    bools = []
    found = {}

    for igs in word:
        i = set(arg).intersection(set(igs))
        bools.append((bool(i), i))
        for ig in igs:
            if ig in arg:
                found.setdefault(ig, 0)
                found[ig] += 1
        # bools.append(i)
        #for vowel in i:
            #print(vowel)
    return found

#search4vowels("e","eer")




def spell(*args):
    mas = sorted(list(map(lambda x: x.lower(), args)),key=len)
    sl = {}
    for i in mas:
        sl[i[0]] = len(i)
    return sl
words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
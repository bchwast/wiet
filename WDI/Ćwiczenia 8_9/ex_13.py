def podzialy(liczba, p=1, s=""):
    if liczba == 0:
        print(s)
    else:
        for i in range(p, liczba+1):
            podzialy(liczba-i, i, s+","+str(i))
#end def


podzialy(7)

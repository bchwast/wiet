def powt(tab1, tab2):
    N1 = len(tab1)
    N2 = len(tab2)
    dl_max = min(N1,N2)
    lis = [0]*(dl_max)
    a = 0
    for i in range(N1):
        for j in range(N2):
            if tab1[i] == tab2[j]:
                lis[a] = tab1[i]
                a += 1
                break
        #end for
    #end for
    dl = 0
    ind = 0
    while lis[ind] > 0:
        dl += 1
        ind += 1
        if ind >= dl_max:
            break
    wynik = [0]*dl
    ind = 0
    while ind < dl:
        wynik[ind] = lis[ind]
        ind += 1
    return wynik

def magmino(tab):
    N = len(tab)
    for i in range(N):
        for j in range(N-1):
            for a in range(N-1):
                if i == a or i == a+1:
                    continue
                for b in range(N):
                    if j == b or j+1 == b:
                        continue
                    klocek1_1 = tab[i][j]
                    klocek1_2 = tab[i][j+1]
                    klocek2_1 = tab[a][b]
                    klocek2_2 = tab[a+1][b]
                    while klocek1_1 != klocek1_2:
                        if klocek1_1 > klocek1_2:
                            klocek1_1 -= klocek1_2
                        else:
                            klocek1_2 -= klocek1_1
                    #end while
                    nwd1 = klocek1_1
                    while klocek2_1 != klocek2_2:
                        if klocek2_1 > klocek2_2:
                            klocek2_1 -= klocek2_2
                        else:
                            klocek2_2 -= klocek2_1
                    #end while
                    nwd2 = klocek2_1
                    while nwd1 != nwd2:
                        if nwd1 > nwd2:
                            nwd1 -= nwd2
                        else:
                            nwd2 -= nwd1
                    #end while
                    if nwd1 == 1:
                        return True
                #end for
            #end for
        #end for
    #end for
    return False
#end def

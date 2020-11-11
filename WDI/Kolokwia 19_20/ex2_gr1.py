def jedynki(t):
    N = len(t)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if k == j:
                    continue
                possible = True
                for wiersz in range(N):
                    if not possible:
                        break
                    if wiersz == i:
                        continue
                    for kolumna in range(N):
                        if not possible:
                            break
                        if kolumna == k or kolumna == j:
                            continue
                        element = t[wiersz][kolumna]
                        jedyneczki = 0
                        while element > 0:
                            if element%2 == 1:
                                jedyneczki += 1
                            element //= 2
                        if jedyneczki%2 == 0:
                            possible = False
                            break
                    #end for
                #end for
                if possible:
                    return True
            #end for
        #end for
    #end for
    return False

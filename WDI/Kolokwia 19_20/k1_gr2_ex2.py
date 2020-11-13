from math import sqrt


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
                        if kolumna == j or kolumna == k:
                            continue
                        element = t[wiersz][kolumna]
                        liczba = 2
                        possible = False
                        while sqrt(liczba) <= element:
                            kwadrat = liczba*liczba
                            while kwadrat <= element:
                                if kwadrat == element:
                                    possible = True
                                    break
                                kwadrat *= liczba
                            liczba += 1
                        #end while
                    #end for
                #end for
                if possible:
                    return True
            #end for
        #end for
    #end for
    return False


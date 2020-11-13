from math import sqrt, ceil


def prime(liczba):
    if liczba == 2 or liczba == 3:
        return True
    if liczba < 2 or liczba%2 == 0 or liczba%3 == 0:
        return True
    a = 5
    while a <= sqrt(liczba):
        if liczba%a == 0:
            return False
        a += 2
        if liczba%a == 0:
            return False
        a += 4
    return True


def kawalki(t1, t2):
    N = len(t1)
    for i in range(N):
        for lenk in range(i,N+1):
            suma1 = 0
            for el1 in range(i,lenk):
                suma1 += el1
            for start in range(N-(lenk-1)):
                suma2 = 0
                for el2 in range(start,lenk):
                    suma2 += el2
                suma = suma1 + suma2
                pierwsze = [0]*int(suma//2)
                ind = 0
                for p in range(2,ceil(sqrt(suma))+1):
                    if prime(p):
                        pierwsze[ind] = p
                        ind += 1
                for p in range(len(pierwsze)):
                    for r in range(len(pierwsze)):
                        if p*r > suma:
                            break
                        if p*r == suma:
                            return True
                    if p > suma//2:
                        break
                #end for
            #end for
        #end for
    #end for
    return False


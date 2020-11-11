from random import randint
from math import sqrt


def kawalki(t1, t2):
    N = len(t1)
    for i in range(N):
        if i + 23 > N:
            end1 = N
        else:
            end1 = i + 23
            for wyc1 in range(i,end1):
                dl_wyc2 = 24 - (end1 - wyc1)
                suma = 0
                for el1 in range(wyc1,end1):
                    suma += t1[el1]
                if dl_wyc2 > N:
                    end2 = N
                else:
                    end2 = dl_wyc2
                for j in range(0,end2):
                    suma_wyc2 = 0
                    for el2 in range(0,dl_wyc2):
                        suma_wyc2 += t2[el2]
                    suma += suma_wyc2
                    podstawa = 2
                    while podstawa <= sqrt(suma):
                        suma_pot = podstawa*podstawa
                        while suma_pot <= suma:
                            if suma_pot == suma:
                                return True
                            suma_pot *= podstawa
                        podstawa += 1
                    #end while
                #end for
            #end for
        #end if
    #end for
    return False

t1 = [randint(1,600) for _ in range(50)]
t2 = [randint(1,600) for _ in range(50)]

print(kawalki(t1,t2))

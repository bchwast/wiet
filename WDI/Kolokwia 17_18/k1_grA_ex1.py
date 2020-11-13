from math import log, ceil


liczba_1 = int(input("> "))
liczba_2 = int(input("> "))

for pdst in range(2, 17):
    l1 = liczba_1
    l2 = liczba_2
    hex = "0123456789ABCDEF"
    num_1 = [0 for _ in range(ceil(log(liczba_1, pdst)))]
    num_2 = [0 for _ in range(ceil(log(liczba_2, pdst)))]
    i = 0
    while l1 > 0:
        num_1[i] = hex[l1%pdst]
        l1 //= pdst
        i += 1
    i = 0
    while l2 > 0:
        num_2[i] = hex[l2%pdst]
        l2 //= pdst
        i += 1
    possible = True
    for a in range(len(num_1)):
        if not possible:
            break
        for b in range(len(num_2)):
            if not possible:
                break
            if num_1[a] == num_2[b]:
                possible = False
                break
        #end for
    #end for
    if possible:
        print(pdst)
        break
#end for
if not possible:
    print("nie ma takiej podstawy")

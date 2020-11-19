from math import sqrt, ceil, log


def prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0 or n%3 == 0:
        return False

    a = 5
    while a <= sqrt(n):
        if n%a == 0:
            return False
        a += 2
        if n%a == 0:
            return False
        a += 4
    #end while
    return True
#end def


def zlozona(n):
    if n <= 3 or n == 5:
        return False
    if n%2 == 0 or n%3 == 0:
        return True

    a = 6
    while a <= n//2:
        if n%(a-1) == 0 or n%(a+1) == 0:
            return True
        a += 6
    #end while
    return False
#end def


def sito(N):
    tab = [True for _ in range(N+1)]
    tab[0] = tab[1] = False

    for i in range(2, ceil(sqrt(N) + 1)):
        if tab[i]:
            for a in range(i*i,N+1,i):
                tab[a] = False
            #end for
        #end if
    #end for

    for i in range(N+1):
        if tab[i]: print(i)
    #end for
#end def


def nwd(a,b):
    a, b = abs(a), abs(b)
    while b != 0:
        b, a = a%b, b
    #end while
    return a
#end def


def co_najmniej_2ga_potega(n):
    podstawa = 2
    while podstawa <= sqrt(n):
        potega = podstawa*podstawa
        while potega <= n:
            if potega == n:
                return True
            potega *= podstawa
        #end while
        podstawa += 1
    #end while
    return False
#end def


def zamiana_podstaw(liczba, podstawa):
    if podstawa < 10:
        new_liczba = 0
        i = 0
        while liczba > 0:
            new_liczba += (liczba%podstawa)*(10**i)
            liczba //= podstawa
            i += 1
        #end while
        return new_liczba
    else:
        new_liczba = ""
        while liczba > 0:
            if liczba%podstawa < 10:
                new_liczba = str(liczba%podstawa) + new_liczba
            #end if
            else:
                new_liczba = str(chr(55+(liczba%podstawa))) + new_liczba
            liczba //= podstawa
        #end while
        return new_liczba
#end def


def zamiana_podstaw_tab(liczba, podstawa):
    if liczba == 0:
        return [0]
    #end if

    hex = "0123456789ABCDEF"
    new_liczba = [0 for _ in range(ceil(log(liczba + 1, podstawa)))]
    i = len(new_liczba) - 1
    while liczba > 0:
        new_liczba[i] = hex[liczba%podstawa]
        liczba //= podstawa
        i -= 1
    #end while
    return new_liczba
#end def


print(zamiana_podstaw_tab(15, 16))


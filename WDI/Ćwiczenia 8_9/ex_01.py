from math import sqrt


def prime(n):
    if n%2 == 0 or n%3 == 0:
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


def wykreslanie(num, i=0):
    if num >= 10 and prime(num):
        print(num)
    #end if
    if num >= 100:
        j = i
        d_num = num
        while num > 10**j:
            c_num = num
            num = num%(10**j) + (num//(10**(j+1)))*(10**j)
            wykreslanie(num, j)
            num = c_num
            j += 1
        #end while
    #end if
#end def


wykreslanie(2137)

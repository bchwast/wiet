from math import sqrt


def prime(num):
    if num == 2 or num == 3: return True
    elif num < 2 or num%2 == 0 or num%3 == 0: return False
    i = 5
    while i < sqrt(num):
        if num%i == 0: return False
        i += 2
        if num%i == 0: return False
        i += 4
    return True


def prog(tab1, tab2):
    n_sum = 0
    n_csum = 0
    mode = [0,1,2]
    sum = 0
    for a in range(N):
        for m in mode:
            if m == 1:
                sum += tab1[a]
                n_sum += 1
                if prime(sum):
                print(sum)
                n_csum += 1


t1 = [1,3,2,4]
t2 = [9,7,4,8]
N = len(t1)
prog(t1,t2)
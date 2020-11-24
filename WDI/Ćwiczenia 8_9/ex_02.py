def waga(n):
    i = 2
    kolejna = True
    w = 0
    while n > 1:
        if n%i == 0:
            if kolejna:
                w += 1
            n //= i
            kolejna = False
        else:
            i += 1
            kolejna = True
    #end while
    return w
#end def


def rownewagi(T):
    def dzielenie(t, n, i=-1, m=0, s_1=0, s_2=0, s_3=0):
        #end if
        if m == 1:
            s_1 += t[i]
        if m == 2:
            s_2 += t[i]
        if m == 3:
            s_3 += t[i]
        #end if
        if i < n - 1:
            if dzielenie(t, n, i+1, 1, s_1, s_2, s_3): return True
            if dzielenie(t, n, i+1, 2, s_1, s_2, s_3): return True
            if dzielenie(t, n, i+1, 3, s_1, s_2, s_3): return True
        else:
            if s_1 == s_2 == s_3:
                return True
    #end def

    N = len(T)
    t_wag = [waga(T[i]) for i in range(N)]
    if dzielenie(t_wag, N):
        return True
    return False
#end def


T = [2, 2, 8, 2, 6]
print(rownewagi(T))
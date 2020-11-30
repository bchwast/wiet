fin = False
def wypisz(t):
    n = len(t)
    for i in range(n):
        print("[",end="")
        for j in range(n-1):
            if t[i][j] < 10:
                print(f"0{t[i][j]}|",end="")
            else:
                print(f"{t[i][j]}|",end="")
        if t[i][n-1] < 10:
            print(f"0{t[i][n-1]}]")
        else:
            print(f"{t[i][n-1]}]")
    print("")
    #end for
#end def


def skoczek(t, n, w, k, r):
    t[w][k] = r
    if r == n**2:
        wypisz(t)
        global fin
        fin = True
        return True
    else:
        for i in range(1, 9):
            if i == 1 and w > 0 and k > 1 and t[w-1][k-2] == 0:     #2lewo1góra
                if skoczek(t, n, w-1, k-2, r+1):
                    return True
            if i == 2 and w > 1 and k > 0 and t[w-2][k-1] == 0:     #1lewo2góra
                if skoczek(t, n, w-2, k-1, r+1):
                    return True
            if i == 3 and w > 1 and k < n-1 and t[w-2][k+1] == 0:   #1prawo2góra
                if skoczek(t, n, w-2, k+1, r+1):
                    return True
            if i == 4 and w > 0 and k < n-2 and t[w-1][k+2] == 0:   #2prawo1góra
                if skoczek(t, n, w-1, k+2, r+1):
                    return True
            if i == 5 and w < n-1 and k < n-2 and t[w+1][k+2] == 0: #2prawo1dół
                if skoczek(t, n, w+1, k+2, r+1):
                    return True
            if i == 6 and w < n-2 and k < n-1 and t[w+2][k+1] == 0: #1prawo2dół
                if skoczek(t, n, w+2, k+1, r+1):
                    return True
            if i == 7 and w < n-2 and k > 0 and t[w+2][k-1] == 0:   #1lewo2dół
                if skoczek(t, n, w+2, k-1, r+1):
                    return True
            if i == 8 and w < n-1 and k > 1 and t[w+1][k-2] == 0:   #2lewo1dół
                if skoczek(t, n, w+1, k-2, r+1):
                    return True
        #end for
        if not fin:
            t[w][k] = 0
#end

t = [[0 for _ in range(5)] for _ in range(5)]

skoczek(t, len(t), 0, 0, 1)

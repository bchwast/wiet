min_s = -1
def szachownica(t, k):
    def przejscie(t, k, s=0, w=0):
        s += t[w][k]
        if w == 7:
            global min_s
            if min_s == -1 or min_s > s:
                min_s = s
        if k > 0 and w < 7:
            przejscie(t, k-1, s, w+1)
        if k < 7 and w < 7:
            przejscie(t, k+1, s, w+1)
        if w < 7:
            przejscie(t, k, s, w+1)
    #end def
    przejscie(t, k)
    return min_s
#end def


t = [[532,26,25,1,64,24,234,25]]*8
print(szachownica(t,0))

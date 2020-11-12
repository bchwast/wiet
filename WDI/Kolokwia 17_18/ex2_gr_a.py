def podciag(tab):
    N = 1000
    dl_max = 0
    for i in range(N):
        if i == 1:
            dl_curr = 1
        else:
            dl_curr = 0
        suma_ind = ind = i
        suma_el = tab[i]
        while ind < (N - 1):
            if tab[ind+1] <= tab[ind] or suma_el + (tab[ind+1]) != suma_ind + (ind + 1):
                break
            suma_el += tab[ind+1]
            suma_ind += (ind + 1)
            ind += 1
            dl_curr += 1
        #end while
        if dl_curr > dl_max:
            dl_max = dl_curr
    #end for
    if dl_max > 1:
        return dl_max
    return 0

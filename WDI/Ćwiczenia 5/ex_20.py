def prawie_jak_tolkien(tab):
    N = len(tab)
    suma_m1 = suma_m2 = 0
    wieza_1 = wieza_2 = None
    for i in range(N):
        row = 0
        for c in range(N):
            row += tab[i][c]
        #end
        for j in range(N):
            col = 0
            for r in range(N):
                col += tab[r][j]
            #end
            col -= tab[i][j]
            row -= tab[i][j]
            if col + row > suma_m1:
                suma_m2 = suma_m1
                suma_m1 = col + row
                wieza_2 = wieza_1
                wieza_1 = (i,j)
            row += tab[i][j]
    return wieza_1, wieza_2

n = int(input("> "))

possible = True
while possible:
    n += 1
    l1 = 1
    l2 = 1
    possible = False
    while not possible and l1 <= n:
        sum = f1 = l1
        f2 = l2
        possible = False
        while sum <= n:
            temp = f1
            f1 = f2
            f2 = temp + f2
            sum += f1
            if sum == n:
                possible = True
        #end while
        tmp = l1
        l1 = l2
        l2 = l2 + tmp
    #end while
#end while
print(n)

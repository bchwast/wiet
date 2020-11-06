a = int(input("> "))
b = int(input("> "))

b2 = b
check = False
count = 0
count2 = 0
count5 = 0
i = 2
while i <= b2:
    while b2 % i == 0:
        if i == 3 or i > 5:
            check = True
        if i == 2:
            count2 += 1
        if i == 5:
            count5 += 1
        b2 //= i
    i += 1

if count2 >= count5:
    count = count2
else:
    count = count5

print(a//b, end=".")
a = a%b

ac = a
bc = b
if check == True:
    while count > 0:
        ac *= 10
        if ac > bc:
            print(ac//bc, end="")
            ac = ac%bc
        else:
            print(0, end="")
        count -= 1

    a = a//(2**count2)
    a = a//(5**count5)
    b = b//(2**count2)
    b = b//(5**count5)

    x = 9
    dig9 = 1
    while x%b != 0:
        x = x*10 + 9
        dig9 += 1

    print("(", end="")
    while dig9 > 0:
        ac *= 10
        if ac > bc:
            print(ac//bc, end="")
            ac = ac%bc
        else:
            print(0, end="")
        dig9 -= 1
    print(")")

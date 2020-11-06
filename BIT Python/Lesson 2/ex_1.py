if __name__ == "__main__":
    a = 2
    b = 3
    print(a, b)

    temp = a
    a = b
    b = temp
    print(a, b)

    c, d = 4, 5
    print(c, d)
    d, c = c, d
    print(c, d)

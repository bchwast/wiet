if __name__ == "__main__":
    p = [" "," "," "," "," "," "," "," "," "]
    print(7 * "-", "\n|" + p[0] + "|" + p[1] + "|" + p[2] + "|", "\n" + 7 * "-", "\n|" + p[3] + "|" + p[4] + "|" + p[5] + "|",
          "\n" + 7 * "-", "\n|" + p[6] + "|" + p[7] + "|" + p[8] + "|", "\n" + 7 * "-")

    while True:
        print("Kolej gracza O")
        pole = int(input("Wybierz pole: "))
        while p[pole-1] != " ":
            pole = int(input("Wybierz inne pole: "))
        p[pole-1] = "O"
        print(7 * "-", "\n|" + p[0] + "|" + p[1] + "|" + p[2] + "|", "\n" + 7 * "-",
              "\n|" + p[3] + "|" + p[4] + "|" + p[5] + "|",
              "\n" + 7 * "-", "\n|" + p[6] + "|" + p[7] + "|" + p[8] + "|", "\n" + 7 * "-")
        if (p[0] == "O" and p[1] == "O" and p[2] == "O") or\
            (p[3] == "O" and p[4] == "O" and p[5] == "O") or\
            (p[6] == "O" and p[7] == "O" and p[8] == "O") or\
            (p[0] == "0" and p[3] == "O" and p[6] == "O") or\
            (p[1] == "O" and p[4] == "O" and p[7] == "O") or\
            (p[2] == "O" and p[5] == "O" and p[8] == "O") or\
            (p[0] == "O" and p[4] == "O" and p[8] == "O") or\
            (p[2] == "O" and p[4] == "O" and p[6] == "O"):
            print("Koniec gry, wygrał gracz O")
            break
        elif p[0] != " " and p[1] != " " and p[2] != " " and\
            p[3] != " " and p[4] != " " and p[5] != " " and\
            p[6] != " " and p[7] != " " and p[8] != " ":
            print("Koniec gry")
            break
        else:
            print("Kolej gracza X")
            pole = int(input("Wybierz pole: "))
            while p[pole-1] != " ":
                pole = int(input("Wybierz inne pole: "))
            p[pole-1] = "X"
            print(7 * "-", "\n|" + p[0] + "|" + p[1] + "|" + p[2] + "|", "\n" + 7 * "-",
                  "\n|" + p[3] + "|" + p[4] + "|" + p[5] + "|",
                  "\n" + 7 * "-", "\n|" + p[6] + "|" + p[7] + "|" + p[8] + "|", "\n" + 7 * "-")
            if (p[0] == "X" and p[1] == "X" and p[2] == "X") or\
                (p[3] == "X" and p[4] == "X" and p[5] == "X") or\
                (p[6] == "X" and p[7] == "X" and p[8] == "X") or\
                (p[0] == "X" and p[3] == "X" and p[6] == "X") or\
                (p[1] == "X" and p[4] == "X" and p[7] == "X") or\
                (p[2] == "X" and p[5] == "X" and p[8] == "X") or\
                (p[0] == "X" and p[4] == "X" and p[8] == "X") or\
                (p[2] == "X" and p[4] == "X" and p[6] == "X"):
                print("Koniec gry, wygrał gracz X")
                break
            elif p[0] != " " and p[1] != " " and p[2] != " " and\
                p[3] != " " and p[4] != " " and p[5] != " " and\
                p[6] != " " and p[7] != " " and p[8] != " ":
                print("Koniec gry")
                break
if __name__ == "__main__":

    search = input("> ")

    with open("colors.txt", "r") as file:
        for line in file.readlines():
            if search in line:
                res = line.split(":")[0]
                check = True

    if check == True:
        print(f"Color name: {res}")
    else:
        print("Color not found")
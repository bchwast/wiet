if __name__ == "__main__":

    shop = []

    with open("data.txt", "r") as file:
        drinks = file.readline()
        drinks = drinks.split(",")
        drinks[-1] = drinks[-1].strip("\n")
        empty = file.readline()

        for line in file.readlines():
            shop.append(line.split(","))
            shop[-1][-1] = shop[-1][-1].strip("\n")

        for i in shop:
            for product in i:
                if product in drinks:
                    drinks.remove(product)

    if drinks == []:
        print("ok")
    else:
        print(drinks)

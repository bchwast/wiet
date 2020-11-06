import os

#def merge:


if __name__ == "__main__":

    text = []
    cat = [i for i in os.listdir() if ".txt" in i]
    cat.sort()
    print(cat)

    for pos in cat:
        with open(pos, "r") as file:
            text.append(file.read())

    for i in range(0,len(cat)-1):
        cat[i] = cat[i].strip(".txt")

    print(cat)

    name =  "_".join(cat)
    print(name)

    with open(name,"a") as file:
        for i in range(0,len(text)-1):
            file.write(f"{text[i]}\n\n---EOF---\n\n")
        file.write(text[-1])
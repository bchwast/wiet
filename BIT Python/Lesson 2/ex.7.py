import json

if __name__ == "__main__":

    with open("example.csv", "r") as file:
        headline = file.readline().split(",")
        headline[-1] = headline[-1].strip("\n")

        tab = []
        lines = file.readlines()
        j = 0
        for line in lines:
            line = line.split(",")
            line[-1] = line[-1].strip("\n")
            lines[j] = line
            j += 1

        for a in range(len(lines)):
            di = {headline[c] : lines[a][c] for c in range(len(headline))}
            tab.append(di)

    with open("example.json", "w") as file:
        json.dump(tab, file)

    print(headline)
    print(lines)
    print(di)
    print(tab)
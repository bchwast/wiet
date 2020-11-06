if __name__ == "__main__":
    string = input("string = ")
    substring = input("substring = ")
    pos = []
    counter = 0

    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            pos.append(i)
            counter += 1

    print(f"{counter} occurrences")
    print(pos)

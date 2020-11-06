def pop(tekst):


if __name__ == "__main__":

    tekst = "ala ma kota kota ma ala ala ala ala psa psa psa"
    tekst = tekst.split(" ")

    tekst_sorted = {}

    for word in tekst:
        tekst_sorted[word] = tekst_sorted.get(word, 0) + 1
    k = 2

    fin = list(tekst_sorted).sort()
    print(tekst)
    print(sorted(tekst_sorted, key=lambda x: tekst_sorted[x], reverse=True)[0:k])
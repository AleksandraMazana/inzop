import string

liczba_dokumentow = int(input())
dokumenty = []

for i in range(liczba_dokumentow):
    dokumenty.append(input())

ile_zapytan = int(input())
zapytania = []

for i in range(ile_zapytan):
    zapytania.append(input())

indeks = dict()
ktory_dokument = 0
for dok in dokumenty:
    wyrazy = dok.split()
    for wyr in wyrazy:
        wyr_przeczyszczony = wyr.lower()
        for znak in string.punctuation:
            wyr_przeczyszczony = wyr_przeczyszczony.replace(znak, '')
        # print (ktory_dokument, wyr_przeczyszczony)
        if wyr_przeczyszczony not in indeks:
            indeks[wyr_przeczyszczony] = dict()
        if ktory_dokument not in indeks[wyr_przeczyszczony]:
            indeks[wyr_przeczyszczony][ktory_dokument] = 1
        else:
            indeks[wyr_przeczyszczony][ktory_dokument] += 1

    ktory_dokument += 1

for zap in zapytania:
    if zap not in indeks:
        print([])
    else:
        lista_wynikowa = list(indeks[zap].items())
        posortowana_lw = sorted(lista_wynikowa, key=lambda x: x[1], reverse=True)
        print([x[0] for x in posortowana_lw])
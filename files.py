class Person(object):
    pass

"""
Napisz klase do ktorej wpisujesz te osoby z pliku
Niech sprawdza czy dane sa w dobrym formacie (3 kolumna powinien byc int, jesli nie jest
niech rzuci ostrzerzenie"
Napisz metody w klasie, ktore zmieniaja wartosci danych pol (typu imie)
Napisz metode ktora printuje dana osobe do zapisu z pliku i uzyj tej metody przy zapisie
"""


if __name__ == "__main__":
    lista = []
    with open('addresses.csv', 'r') as file1:
        for line in file1:
            lista.append(line.strip().split(","))

    for item in lista:
        item[0] = item[0].upper()

    list_with_strings = [",".join(x) for x in lista]


    new_file_name = "modified_adresses.txt"
    with open(new_file_name, "w") as file2:
        file2.write('\n'.join(list_with_strings) + '\n')
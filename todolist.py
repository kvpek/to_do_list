def dodaj_zadanie(opis):
    zadanie = {"opis" : opis, "status" : False}
    return zadanie

import csv 
def zapisz_zadanie(zadanie):
    with open("todo.csv", "a", newline='') as plik:
        writer = csv.writer(plik)
        writer.writerow([zadanie["opis"], zadanie["status"]])
    
    
def pokaz_zadania():
    with open("todo.csv", "r") as plik:
        reader = csv.reader(plik)
        for index, row in enumerate(reader, start=1):
            status = "[x]" if row[1] == "True" else "[]"
            print(f"{index}, {status} {row[0]}")
            
def oznacz_jako_zrobione(numer_zadania):
    with open("todo.csv", "r") as plik:
        reader = csv.reader(plik)
        zadania = list(reader)
        zadania[numer_zadania - 1] [1] = "True"
    with open("todo.csv", "w", newline ='') as plik:
        writer = csv.writer(plik)
        writer.writerows(zadania)
        
def usun_zadanie(numer_zadania):
    with open("todo.csv", "r") as plik:
        reader = csv.reader(plik)
        zadania = list(reader)
        del zadania[numer_zadania - 1]
    with open("todo.csv", "w", newline='') as plik:
        writer = csv.writer(plik)
        writer.writerows(zadania)
        
while True:
    try:
        print("1. Pokaz liste zadan.")
        print("2. Dodaj nowe zadanie.")
        print("3. Oznacz jako zrobione.")
        print("4. Usun zadanie.") 
        print("5. Zakoncz.")
        x = int(input("To do list. Wybierz działanie, które chcesz wykonać: "))
            
        if x == 1:
            print("Lista zadan:")
            pokaz_zadania()
            
        if x == 2:
            opis = input("Wpisz tresc zadania: ")
            zadanie = dodaj_zadanie(opis)
            zapisz_zadanie(zadanie)
            
        if x == 3:
            numer = int(input("Podaj numer zadania do oznaczenia jako zrobione: "))
            oznacz_jako_zrobione(numer)

        if x == 4:
            numer = int(input("Podaj numer zadania do usuniecia: "))
            usun_zadanie(numer)
            
        if x == 5:
            break
    
    except ValueError:
        print("Błąd")
    
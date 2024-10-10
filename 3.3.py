# Dla każdej z liczb z drugiego wiersza rozstrzygnij, czy da się ją przedstawić jako iloczyn jedynie liczb z pierwszego wiersza. Przy tym liczba wystąpień danego czynnika w iloczynie nie może być większa niż liczba wystąpień tego czynnika w pierwszym wierszu. Znajdź wszystkie liczby, które da się tak przedstawić, i je wypisz.
from collections import Counter
import math

def znajdz_liczby_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        pierwszy_wiersz = list(map(int, plik.readline().split()))
        drugi_wiersz = list(map(int, plik.readline().split()))

    czynniki_pierwszego_wiersza = Counter(pierwszy_wiersz)
    wynik = []

    for liczba in drugi_wiersz:
        n = liczba
        czynniki_liczby = []
        
        # rozkład liczby na czynniki pierwsze
        while n % 2 == 0:
            czynniki_liczby.append(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                czynniki_liczby.append(i)
                n //= i
        if n > 2:
            czynniki_liczby.append(n)

        licznik_czynnikow = Counter(czynniki_liczby)
        czy_mozna = True

        # sprawdzanie czy liczba może być złożona z liczb w pierwszym wierszu
        for czynnik, ilosc in licznik_czynnikow.items():
            if czynniki_pierwszego_wiersza[czynnik] < ilosc:
                czy_mozna = False
                break
        
        if czy_mozna:
            wynik.append(liczba)
    
    return wynik

nazwa_pliku = 'liczby.txt'
wynik = znajdz_liczby_z_pliku(nazwa_pliku)
print(wynik)


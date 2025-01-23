# NWD (Największy Wspólny Dzielnik)

## Opis
Ten skrypt oblicza największy wspólny dzielnik (NWD) dwóch liczb całkowitych za pomocą algorytmu iteracyjnego opartego na odejmowaniu.

## Jak działa
1. Użytkownik wprowadza dwie liczby całkowite: `a` i `b`.
2. Algorytm iteracyjnie oblicza NWD zgodnie z poniższymi zasadami:
   - Jeśli `a > b`, od `a` odejmowana jest wartość `b`.
   - Jeśli `b > a`, od `b` odejmowana jest wartość `a`.
   - Proces powtarza się, aż `a` będzie równe `b`.
3. Ostateczna wartość `a` (lub `b`) jest największym wspólnym dzielnikiem.
4. Wynik zostaje wyświetlony na ekranie.

## Przykład użycia
Po uruchomieniu skryptu użytkownik zostanie poproszony o podanie dwóch liczb:
```
podaj liczbę a: 56
podaj liczbę b: 98
```
Wynik działania skryptu:
```
14
```

## Kod
```python
def nwd(a,b):
    # sprawdź czy obydwie liczby są dodatnie
    if a>0 and b>0:
        # podczas gdy (a) nie jest równe (b)
        while a != b:
            # jeśli (a) jest większe od (b), odejmij (b) od (a)
            if a > b:
                a -= b
            # inaczej, odejmij (a) od (b)
            else:
                b -= a
        # zwróć wartość
        return a
    # jeśli liczby nie są dodatnie, zwróć błąd
    else:
        return "błąd"
# zdobądź i zwróć dane
a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))
print(str(nwd(a,b)))
```

## Uwagi
- Algorytm ten działa poprawnie dla dodatnich liczb całkowitych.
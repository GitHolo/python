# NWD (Największy Wspólny Dzielnik) - Algorytm Euklidesa

## Opis
Ten skrypt oblicza największy wspólny dzielnik (NWD) dwóch liczb całkowitych przy użyciu algorytmu Euklidesa opartego na operacji modulo.

## Jak działa
1. Użytkownik wprowadza dwie liczby całkowite: `a` i `b`.
2. Algorytm iteracyjnie oblicza resztę z dzielenia `a` przez `b` i przypisuje:
   - `b` do `a`,
   - resztę do `b`.
3. Proces powtarza się, aż `b` osiągnie wartość `0`.
4. Ostateczna wartość `a` jest największym wspólnym dzielnikiem.
5. Wynik zostaje wyświetlony na ekranie.

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
def euclideanNWD(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a

a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))
print(euclideanNWD(a, b))
```

## Uwagi
- Algorytm Euklidesa jest bardziej wydajny niż metoda oparta na odejmowaniu.
- Skrypt działa poprawnie dla dodatnich liczb całkowitych.
- Wartości `a` i `b` mogą być dowolne, ale obliczenia są przeprowadzane dla wartości bezwzględnych.

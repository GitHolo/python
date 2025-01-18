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
    if a>0 and b>0:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    else:
        return "błąd"

a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))
print(str(nwd(a,b)))
```

## Uwagi
- Algorytm ten działa poprawnie dla dodatnich liczb całkowitych.
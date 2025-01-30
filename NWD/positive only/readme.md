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


## Uwagi
- Algorytm ten działa poprawnie dla dodatnich liczb całkowitych.


### [Python](./script.py)
```python
def nwd(a, b):
    if a > 0 and b > 0:  # Sprawdzanie, czy liczby są większe od zera
        while a != b:  # Dopóki liczby są różne
            if a > b:
                a -= b  # Odejmowanie mniejszej liczby od większej
            else:
                b -= a  # Odejmowanie mniejszej liczby od większej
        return a  # Zwrócenie największego wspólnego dzielnika
    else:
        return "błąd"  # Zwrócenie komunikatu o błędzie, jeśli liczby są <= 0
```

### [Ruby](./script.rb)
```ruby
def nwd(a, b)
  if a > 0 && b > 0  # Sprawdzanie, czy liczby są większe od zera
    while a != b  # Dopóki liczby są różne
      if a > b
        a -= b  # Odejmowanie mniejszej liczby od większej
      else
        b -= a  # Odejmowanie mniejszej liczby od większej
      end
    end
    return a  # Zwrócenie największego wspólnego dzielnika
  else 
    return "błąd"  # Zwrócenie komunikatu o błędzie, jeśli liczby są <= 0
  end
end
```

## Różnice między Pythonem a Ruby:
1. **Składnia operacji warunkowych:**
   - W Pythonie używamy `if a > 0 and b > 0`, aby sprawdzić, czy obie liczby są większe od zera.
   - W Ruby używamy `if a > 0 && b > 0` z podwójnym `&` do logicznego sprawdzenia warunku.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
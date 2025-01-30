# Funkcja Dzielniki (divisor)

## Opis
Funkcja `divisor` oblicza dzielniki liczby `a` i zwraca je w formie listy. Działa poprzez dzielenie liczby `a` przez kolejne liczby, zaczynając od 2, a następnie od liczb nieparzystych. W przypadku gdy liczba nie jest podzielna, przechodzi do kolejnej liczby.

## Jak działa
1. Funkcja przyjmuje liczbę `a` jako argument.
2. Jeśli liczba jest podzielna przez 2, dodaje 2 do listy dzielników i dzieli liczbę `a` przez 2.
3. Następnie sprawdza dzielniki nieparzyste zaczynając od 3, iterując do pierwiastka kwadratowego z `a`.
4. Jeśli pozostała liczba `a` jest większa niż 1, dodaje ją do listy dzielników.
5. Funkcja zwraca listę dzielników liczby `a`.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może obliczyć dzielniki liczby:
```
divisor(60)  # [2, 2, 3, 5]
```

## Kod

### [Python](./script.py)
```python
import math

def divisor(a):
    result = []  # Lista przechowująca dzielniki
    while a % 2 == 0:  # Sprawdzanie dzielników 2
        result.append(2)
        a //= 2  # Dzielenie liczby przez 2
    for i in range(3, int(math.sqrt(a)) + 1, 2):  # Iteracja przez liczby nieparzyste
        while a % i == 0:  # Jeśli liczba jest podzielna przez i
            result.append(i)  # Dodaje i do listy dzielników
            a //= i  # Dzielenie liczby przez i
    if a > 1:  # Jeśli pozostała liczba jest większa niż 1
        result.append(a)  # Dodaje ją do listy dzielników
    return result  # Zwraca listę dzielników
```

### [Ruby](./script.rb)
```ruby
def divisor(a)
  result = []  # Lista przechowująca dzielniki
  while a % 2 == 0  # Sprawdzanie dzielników 2
    result << 2  # Dodaje 2 do listy dzielników
    a /= 2  # Dzielenie liczby przez 2
  end
  (3..Math.sqrt(a)+1).step(2) do |i|  # Iteracja przez liczby nieparzyste
    while a % i == 0  # Jeśli liczba jest podzielna przez i
      result << i.to_i  # Dodaje i do listy dzielników
      a /= i  # Dzielenie liczby przez i
    end
  end
  if a > 1  # Jeśli pozostała liczba jest większa niż 1
    result << a.to_i  # Dodaje ją do listy dzielników
  end
  return result  # Zwraca listę dzielników
end
```

## Różnice między Pythonem a Ruby:
1. **Składnia operacji dzielenia:**
   - W Pythonie używamy `a //= 2` i `a //= i`, aby zaktualizować wartość `a` po podzieleniu przez 2 lub `i` (dzielenie całkowite).
   - W Ruby używamy `a /= 2` i `a /= i`, co wykonuje dzielenie z przypisaniem (nie musi być to dzielenie całkowite, choć w tym przypadku działa podobnie).

2. **Iteracja przez liczby nieparzyste:**
   - W Pythonie używamy `range(3, int(math.sqrt(a)) + 1, 2)`, co generuje liczby nieparzyste od 3 do pierwiastka kwadratowego z `a`.
   - W Ruby używamy `(3..Math.sqrt(a)+1).step(2)` do iteracji przez liczby nieparzyste. Składnia `step(2)` jest idiomatyczna dla Ruby i pozwala na łatwą iterację co 2.

3. **Zwracanie listy dzielników:**
   - W Pythonie używamy `return result` do zwrócenia listy dzielników.
   - W Ruby funkcje zwracają ostatnią wartość, więc `result` jest zwracane automatycznie, ale dla jasności dodano `return result`.

4. **Użycie `math.sqrt`:**
   - W Pythonie korzystamy z funkcji `math.sqrt(a)` do obliczenia pierwiastka kwadratowego z `a`, gdzie sam `math` musi być najpierw zimportowany do kodu poprzez `import math`.
   - W Ruby używamy `Math.sqrt(a)` do uzyskania tego samego wyniku, przy czym `Math` jest domyślnie dostępny.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
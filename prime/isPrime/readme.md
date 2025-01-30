# Funkcja Sprawdzająca Liczbę Pierwszą (isPrime)

## Opis
Funkcja `isPrime` sprawdza, czy dana liczba `n` jest liczbą pierwszą. Liczba pierwsza to taka, która jest większa niż 1 i dzieli się tylko przez 1 oraz przez siebie. Funkcja iteruje przez liczby od 2 do pierwiastka kwadratowego z `n` i sprawdza, czy `n` jest podzielna przez którąkolwiek z nich.

## Jak działa
1. Funkcja przyjmuje liczbę `n` jako argument.
2. Jeśli liczba `n` jest podzielna przez jakąkolwiek liczbę w zakresie od 2 do pierwiastka kwadratowego z `n`, funkcja zwraca `False`, oznaczając, że liczba nie jest pierwsza.
3. Jeśli nie znaleziono żadnego dzielnika, funkcja zwraca `True`, oznaczając, że liczba jest pierwsza.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może sprawdzić, czy liczba jest pierwsza:
```
isPrime(7)  # True
isPrime(10) # False
```

## Kod

### [Python](./script.py)
```python
def isPrime(n):
    for i in range(2, int(n**0.5) + 1):  # Iteruje przez liczby od 2 do pierwiastka kwadratowego z n
        if n % i == 0:  # Jeśli n jest podzielne przez i, nie jest liczbą pierwszą
            return False
    return True  # Jeśli nie znaleziono dzielnika, n jest liczbą pierwszą
```

### [Ruby](./script.rb)
```ruby
def isPrime(n)
  (2...(n**0.5)+1).each do |i|  # Iteruje przez liczby od 2 do pierwiastka kwadratowego z n
    if n % i == 0  # Jeśli n jest podzielne przez i, nie jest liczbą pierwszą
      return false
    end
  end
  return true  # Jeśli nie znaleziono dzielnika, n jest liczbą pierwszą
end
```

## Różnice między Pythonem a Ruby:
1. **Pętla `for`/`each`:**
   - W Pythonie używamy pętli `for` z zakresem `range(2, int(n**0.5) + 1)` do iterowania przez liczby od 2 do pierwiastka kwadratowego z `n`.
   - W Ruby zamiast `for` stosujemy metodę `each` na zakresie `(2...(n**0.5)+1)`.

2. **Zakres pętli:**
   - W Pythonie zakres iteracji tworzymy za pomocą funkcji `range(2, int(n**0.5) + 1)`, która generuje liczby od 2 do pierwiastka kwadratowego z `n` (włącznie).
   - W Ruby używamy składni `(2...(n**0.5)+1)`, która jest idiomatycznym sposobem w Ruby na stworzenie zakresu.

3. **Zwracanie wartości:**
   - W Pythonie, jeśli liczba nie jest pierwsza, funkcja zwraca `False`, a jeśli jest, zwraca `True`.
   - W Ruby działa to podobnie, zwracając `false` lub `true` w zależności od wyniku.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
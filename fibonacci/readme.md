# Funkcja Generująca Ciąg Fibonacciego

## Opis
Funkcja `fibonacci` generuje ciąg Fibonacciego do podanej liczby `max`, która określa ilość liczb w ciągu. Ciąg Fibonacciego to sekwencja, w której każda liczba (oprócz dwóch pierwszych) jest sumą dwóch poprzednich.

## Jak działa
1. Funkcja przyjmuje `max` jako liczba elementów, które mają zostać wygenerowane w ciągu Fibonacciego.
2. Funkcja rozpoczyna od wartości `0` i `1`.
3. Następnie w pętli dodaje kolejne liczby, które są sumą dwóch poprzednich.
4. Proces trwa, aż osiągniemy pożądaną liczbę elementów (`max`).

## Przykład użycia
Po uruchomieniu skryptu użytkownik może obliczyć ciąg Fibonacciego do określonego limitu:
```
fibonacci(6)  # [0, 1, 1, 2, 3, 5]
```

## Kod

### [Python](./script.py)
```python
def fibonacci(max: int):
    result = [0]  # Rozpoczynamy od liczby 0
    first = 0
    second = 1

    while max > 0:
        first, second = second, first + second  # Obliczamy kolejną liczbę Fibonacciego
        result.append(first)  # Dodajemy liczbę do wyniku
        max -= 1  # Zmniejszamy licznik

    return result  # Zwracamy wygenerowany ciąg
```

### [Ruby](./script.rb)
```ruby
def fibonacci(max)
  result = [0]  # Rozpoczynamy od liczby 0
  first = result[0]
  second = first + 1

  while max > 0
    first, second = second, first + second  # Obliczamy kolejną liczbę Fibonacciego
    result << first  # Dodajemy liczbę do wyniku
    max -= 1  # Zmniejszamy licznik
  end
  return result  # Zwracamy wygenerowany ciąg
end
```

## Różnice między Pythonem a Ruby:
1. **Dodawanie nowych elementów do listy:**
   - W Pythonie używamy `result.append(first)` do dodania nowej liczby do listy.
   - W Ruby używamy `result << first` do dodania nowego elementu do tablicy.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.



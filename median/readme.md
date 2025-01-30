# Funkcja Obliczania Mediany

## Opis
Funkcja `median` oblicza medianę z listy liczb. Mediana to środkowa wartość w posortowanym zbiorze danych. Jeśli liczba elementów w zbiorze jest nieparzysta, mediana to środkowa liczba, natomiast jeśli jest parzysta, mediana to średnia dwóch środkowych liczb.

## Jak działa
1. Funkcja przyjmuje listę liczb `arr` jako argument.
2. Lista liczb jest sortowana w porządku rosnącym.
3. Jeśli liczba elementów w posortowanej liście jest nieparzysta, mediana to środkowy element listy.
4. Jeśli liczba elementów jest parzysta, mediana to średnia dwóch środkowych elementów.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może obliczyć medianę z listy liczb:
```
median([3, 1, 2, 4, 5])  # 3
median([3, 1, 2, 4])  # 2.5
```

## Kod

### [Python](./script.py)
```python
def median(arr: list):
    n = int(len(arr))  # Długość listy
    arr.sort()  # Sortowanie listy
    if n % 2 == 0:  # Jeśli liczba elementów jest parzysta
        n /= 2
        return arr[int((n + (n + 1)) / 2) - 1]  # Średnia dwóch środkowych elementów
    else:  # Jeśli liczba elementów jest nieparzysta
        return arr[int((n + 1) / 2)]  # Środkowy element
```

### [Ruby](./script.rb)
```ruby
def median(arr)
  n = arr.length  # Długość listy
  arr = arr.sort  # Sortowanie listy
  if n % 2 == 0  # Jeśli liczba elementów jest parzysta
    n /= 2
    return arr[(n + (n + 1)) / 2 - 1]  # Średnia dwóch środkowych elementów
  else  # Jeśli liczba elementów jest nieparzysta
    return arr[(n + 1) / 2]  # Środkowy element
  end
end
```

## Różnice między Pythonem a Ruby:
1. **Długość listy:**
   - W Pythonie długość listy obliczamy za pomocą `n = int(len(arr))`.
   - W Ruby używamy `n = arr.length`.

2. **Sortowanie listy:**
   - W Pythonie używamy `arr.sort()` do posortowania listy.
   - W Ruby używamy `arr.sort` do tego samego celu.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.

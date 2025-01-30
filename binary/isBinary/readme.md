# Funkcja Sprawdzająca, Czy Liczba Jest Binarna

## Opis
Funkcja `isBinary` sprawdza, czy dana liczba jest zapisana w systemie binarnym. Liczba binarna to liczba, która składa się wyłącznie z cyfr `0` i `1`.

## Jak działa
1. Funkcja konwertuje liczbę na ciąg znaków, aby sprawdzić, czy składa się wyłącznie z cyfr `0` i `1`.
2. Dla każdego znaku w ciągu sprawdza, czy jest to `0` lub `1`.
3. Jeśli którykolwiek znak nie jest liczbą binarną, funkcja zwraca `False`.
4. Jeśli wszystkie znaki są `0` lub `1`, funkcja zwraca `True`.

## Przykład użycia
Po uruchomieniu skryptu, użytkownik może sprawdzić, czy liczba jest liczbą binarną:
```
isBinary(10101)  # True
isBinary(12345)  # False
```

## Kod

### Python
```python
def isBinary(n: int):
    for i in str(n):  # Iterujemy przez każdy znak liczby
        if str(i) not in ['0', '1']:  # Sprawdzamy, czy znak nie jest ani '0', ani '1'
            return False  # Jeśli znajdziemy inny znak, zwracamy False
    return True  # Jeśli wszystkie znaki są '0' lub '1', zwracamy True
```

### Ruby
```ruby
def isBinary(n)
  n.to_s.each_char do |i|  # Iterujemy przez każdy znak liczby
    if !['0', '1'].include?(i.to_s)  # Sprawdzamy, czy znak nie jest ani '0', ani '1'
      return false  # Jeśli znajdziemy inny znak, zwracamy false
    end
  end
  return true  # Jeśli wszystkie znaki są '0' lub '1', zwracamy true
end
```

## Różnice między Pythonem a Ruby:
1. **Konwersja liczby na ciąg znaków:**
   - W Pythonie używamy `str(n)` do konwersji liczby na ciąg znaków.
   - W Ruby używamy `n.to_s` w celu przekształcenia liczby na ciąg znaków.

2. **Iteracja przez znaki liczby:**
   - W Pythonie iterujemy po każdym znaku za pomocą pętli `for i in str(n)`.
   - W Ruby stosujemy metodę `each_char` do iteracji po każdym znaku w ciągu.

3. **Sprawdzanie obecności cyfr '0' lub '1':**
   - W Pythonie używamy `if str(i) not in ['0', '1']` do sprawdzenia, czy znak jest różny od '0' i '1'.
   - W Ruby używamy `if !['0', '1'].include?(i.to_s)` do tego samego celu.


## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
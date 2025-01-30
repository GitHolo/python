# Funkcja Armstronga

## Opis
Funkcja `armstrong` sprawdza, czy podana liczba jest liczbą Armstronga. Liczba Armstronga to liczba, która jest równa sumie swoich cyfr podniesionych do odpowiedniej potęgi. Na przykład liczba 153 to liczba Armstronga, ponieważ \(1^3 + 5^3 + 3^3 = 153\).

## Jak działa
1. Funkcja iteruje przez wszystkie cyfry liczby, podnosi je do odpowiednich potęg i sumuje je.
2. Jeżeli suma jest równa początkowej liczbie, zwraca `True`.
3. W przeciwnym przypadku zwraca `False`.

## Przykład użycia
```
armstrong(153)  # Zwraca True
armstrong(123)  # Zwraca False
```

## Kod

### Python(./script.py)
```python
def armstrong(num: int):
    # Inicjalizacja zmiennej 'factor', która będzie odpowiadać za potęgę, do której podnosimy cyfry.
    factor = 0
    # Zmienna 'result' przechowuje sumę cyfr podniesionych do odpowiednich potęg.
    result = 0
    # Pętla wykonuje się, dopóki suma cyfr podniesionych do odpowiednich potęg jest mniejsza niż 'num'.
    while result < num:
        # Obliczamy sumę cyfr liczby 'num', każdą cyfrę podnosimy do potęgi 'factor'.
        result = sum(int(digit) ** factor for digit in str(num))
        # Zwiększamy potęgę, aby w następnym kroku podnieść cyfry do wyższej potęgi.
        factor += 1
        # Sprawdzamy, czy suma cyfr podniesionych do odpowiednich potęg równa się liczbie 'num'.
        if result == num:
            # Jeśli tak, to zwracamy True, ponieważ liczba jest liczbą Armstronga.
            return True
    # Jeśli nie znaleziono liczby Armstronga, zwracamy False.
    return False
```

### Ruby
```ruby
def armstrong(num)
  # Inicjalizacja zmiennej 'factor', która będzie odpowiadać za potęgę, do której podnosimy cyfry.
  factor = 0
  # Zmienna 'result' przechowuje sumę cyfr podniesionych do odpowiednich potęg.
  result = 0
  # Pętla wykonuje się, dopóki suma cyfr podniesionych do odpowiednich potęg jest mniejsza niż 'num'.
  while result < num
    # Obliczamy sumę cyfr liczby 'num', każdą cyfrę podnosimy do potęgi 'factor'.
    result = num.to_s.chars.map { |digit| digit.to_i ** factor }.sum
    # Zwiększamy potęgę, aby w następnym kroku podnieść cyfry do wyższej potęgi.
    factor += 1
    # Sprawdzamy, czy suma cyfr podniesionych do odpowiednich potęg równa się liczbie 'num'.
    return true if result == num
  end
  # Jeśli nie znaleziono liczby Armstronga, zwracamy false.
  return false
end
```

## Różnice między Pythonem a Ruby:
1. **Konwersja liczby na cyfry:**
   - W Pythonie używamy `str(num)` do konwersji liczby na łańcuch, a potem iterujemy przez cyfry w łańcuchu.
   - W Ruby używamy `num.to_s.chars`, aby przekonwertować liczbę na ciąg znaków i uzyskać tablicę z cyframi.

2. **Podnoszenie cyfr do potęgi:**
   - W Pythonie używamy generatora w funkcji `sum()`, który oblicza sumę cyfr podniesionych do odpowiedniej potęgi: `sum(int(digit) ** factor for digit in str(num))`.
   - W Ruby używamy metody `map`, która mapuje każdą cyfrę na jej wartość podniesioną do odpowiedniej potęgi, a potem sumujemy te wartości za pomocą metody `sum`.

3. **Wartości warunkowe:**
   - W Pythonie stosujemy `if result == num`, aby sprawdzić, czy liczba Armstronga została znaleziona.
   - W Ruby mamy `return true if result == num`, co natychmiast kończy działanie funkcji, jeśli liczba Armstronga została znaleziona.



## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
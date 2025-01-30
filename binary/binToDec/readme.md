# Funkcja Konwersji Liczby Binarnej na Dziesiętną

## Opis
Funkcja `binToDec` konwertuje liczbę binarną na liczbę dziesiętną. Funkcja sprawdza, czy podana liczba jest liczbą binarną, a następnie konwertuje ją na dziesiętną, sumując odpowiednie potęgi liczby 2.

## Jak działa
1. Funkcja sprawdza, czy liczba jest binarna, wywołując funkcję `isBinary`.
2. Dzieli liczbę przez 10, zaczynając od najmniej znaczącego bitu, i sumuje odpowiednie potęgi liczby 2.
3. Zwraca wynik konwersji na liczbę dziesiętną.

## Przykład użycia
```
binToDec(1010)  # Wynik: 10
binToDec(0)     # Wynik: 0
```

## Kod

### [Python](./script.py)
```python
def binToDec(bin: float):
    if isBinary(bin):
        bin = float(bin)
        result = 0
        n = 0
        while bin != 0:
            if bin % 10 != 0:
                result += 2**n
            bin //= 10
            n += 1
        return result
```

### [Ruby](./script.rb)
```ruby
def binToDec(bin)
  return "błąd" unless isBinary(bin)

  bin = bin.to_i
  result = 0
  n = 0

  while bin != 0
    if bin % 10 != 0
      result += 2**n
    end
    bin /= 10
    n += 1
  end

  return result
end
```

## Różnice między Pythonem a Ruby:
1. **Zwracanie wartości "błąd":**
   - W Pythonie, jeśli liczba nie jest binarna, funkcja nie zwraca wartości błędu bezpośrednio, ale wymaga wcześniejszego sprawdzenia przez funkcję `isBinary`.
   - W Ruby, jeśli liczba nie jest binarna, zwracamy "błąd" za pomocą: `return "błąd" unless isBinary(bin)`.


## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
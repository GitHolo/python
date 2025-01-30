# Funkcja Największy Wspólny Dzielnik (NWD) - Algorytm Euklidesa

## Opis
Funkcja `euclideanNWD` oblicza największy wspólny dzielnik dwóch liczb `a` i `b` za pomocą algorytmu Euklidesa. Algorytm polega na tym, że w każdym kroku zastępujemy większą liczbę resztą z dzielenia większej liczby przez mniejszą, aż jedna z liczb stanie się zerem. Wtedy druga liczba jest największym wspólnym dzielnikiem.

## Jak działa
1. Funkcja przyjmuje dwie liczby `a` i `b` jako argumenty.
2. Dopóki `b` nie jest równe zeru, funkcja oblicza resztę z dzielenia `a` przez `b` i przypisuje ją do `r`.
3. Następnie zamienia wartości `a` i `b` (wartość `b` zostaje zastąpiona resztą `r`).
4. Kiedy `b` stanie się zerem, wartość `a` jest największym wspólnym dzielnikiem.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może obliczyć NWD dwóch liczb:
```
euclideanNWD(56, 98)  # 14
```

## Kod

### [Python](./script.py)
```python
def euclideanNWD(a, b):
    while b != 0:  # Dopóki b nie jest zerem
        r = a % b  # Obliczamy resztę z dzielenia
        a, b = b, r  # Zamiana a i b
    return a  # Zwrócenie największego wspólnego dzielnika
```

### [Ruby](./script.rb)
```ruby
def euclideanNWD(a, b)
  while b != 0  # Dopóki b nie jest zerem
    r = a % b  # Obliczamy resztę z dzielenia
    a, b = b, r  # Zamiana a i b
  end
  return a  # Zwrócenie największego wspólnego dzielnika
end
```


## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
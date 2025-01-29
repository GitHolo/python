# Rozkład na czynniki pierwsze

## Opis funkcji

Ten skrypt służy do rozkładu liczby całkowitej na czynniki pierwsze. Wprowadź dowolną liczbę całkowitą, a program zwróci listę jej dzielników pierwszych.

## Jak działa skrypt?

1. Skrypt sprawdza, czy liczba jest podzielna przez 2, i dodaje 2 do wyników tyle razy, ile występuje w rozkładzie.
2. Następnie sprawdza dzielniki pierwsze od 3 do pierwiastka kwadratowego z liczby.
3. Jeśli po tych operacjach pozostanie liczba większa niż 1, oznacza to, że jest to liczba pierwsza.

## Przykład

Dla liczby `28`, skrypt zwróci:

```plaintext
[2, 2, 7]
```

## Kod
```python
import math

def divisor(a):
    result = []
    while a%2==0:
        result.append(2)
        a//=2
    for i in range(3, int(math.sqrt(a))+1, 2):
        while a%i==0:
            result.append(i)
            a//=i
    if a>1:
        result.append(a)
    return result
  

a = int(input("Wpisz liczbę: "))
print("dzielniki liczby: "+str(divisor(a)))      
```

## Jak uruchomić?

1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
3. Otrzymasz listę dzielników pierwszych w konsoli.

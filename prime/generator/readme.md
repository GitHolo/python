# Funkcja Generująca Liczby Pierwsze (primeGen)

## Opis
Funkcja `primeGen` generuje pierwsze `max` liczb pierwszych. Rozpoczyna od liczby 2 i iteruje przez kolejne liczby, sprawdzając, czy są liczbami pierwszymi, aż znajdzie wymaganą ilość liczb pierwszych.

## Jak działa
1. Funkcja przyjmuje parametr `max`, który określa, ile liczb pierwszych ma zostać wygenerowanych.
2. Funkcja iteruje przez kolejne liczby, zaczynając od 2, i sprawdza, czy są liczbami pierwszymi za pomocą funkcji `isPrime`.
3. Jeśli liczba jest pierwsza, dodaje ją do listy `primes` i zmniejsza wartość `max` o 1.
4. Proces ten powtarza się, aż lista `primes` zawiera `max` liczb pierwszych.
5. Funkcja zwraca listę liczb pierwszych.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może podać, ile liczb pierwszych chce wygenerować:
```
primeGen(5)  # [2, 3, 5, 7, 11]
```

## Kod

### Python
```python
def primeGen(max):
    primes = []  # Lista przechowująca liczby pierwsze
    num = 2  # Pierwsza liczba do sprawdzenia
    
    while max > 0:  # Powtarza, dopóki nie znajdziemy wymaganej liczby liczb pierwszych
        if isPrime(num):  # Sprawdza, czy liczba jest pierwsza
            primes.append(num)  # Dodaje liczbę do listy primes
            max -= 1  # Zmniejsza licznik
        num += 1  # Przechodzi do kolejnej liczby
    
    return primes  # Zwraca listę liczb pierwszych
```

### Ruby
```ruby
def primeGen(max)
  primes = []  # Lista przechowująca liczby pierwsze
  num = 2  # Pierwsza liczba do sprawdzenia

  while max > 0  # Powtarza, dopóki nie znajdziemy wymaganej liczby liczb pierwszych
    if isPrime(num)  # Sprawdza, czy liczba jest pierwsza
      primes.append(num)  # Dodaje liczbę do listy primes
      max -= 1  # Zmniejsza licznik
    end
    num += 1  # Przechodzi do kolejnej liczby
  end

  return primes  # Zwraca listę liczb pierwszych
end
```

## Różnice między Pythonem a Ruby:
1. **Pętla `while`:**
   - W Pythonie pętla `while max > 0` jest używana w sposób tradycyjny, z warunkiem na początku pętli.
   - W Ruby składnia jest podobna, ale używamy słowa kluczowego `end` do zamknięcia pętli, co jest specyficzne dla Ruby.

2. **Dodawanie elementów do listy:**
   - W Pythonie używamy metody `append()` do dodawania elementów do listy, np. `primes.append(num)`.
   - W Ruby używamy metody `append()` w tej samej formie, np. `primes.append(num)`, ale składnia Ruby jest bardziej idiomatyczna, z dodatkowymi opcjami dodawania elementów, np. `<<`.

3. **Struktura kończenia bloków:**
   - W Pythonie blok pętli `while` jest zakończony słowem kluczowym `return`.
   - W Ruby blok pętli `while` jest zakończony słowem kluczowym `end`, a następnie zwracamy wynik za pomocą `return`.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
# Funkcja Odejmowania Liczb Binarnych

## Opis
Funkcja `subtractBinary` wykonuje operację odejmowania dwóch liczb binarnych. Jeśli jedna z liczb jest mniejsza od drugiej, funkcja zwraca komunikat, że wynik byłby ujemny. Funkcja obsługuje pożyczanie bitów, podobnie jak w tradycyjnym odejmowaniu liczb w systemie dziesiętnym.

## Jak działa
1. Funkcja sprawdza, czy obie liczby wejściowe są liczbami binarnymi.
2. Jeśli któraś z liczb jest mniejsza od drugiej, funkcja zwraca komunikat o niemożności wykonania operacji.
3. Funkcja przeprowadza odejmowanie bit po bicie, stosując pożyczanie w przypadku, gdy wynik odjęcia jest mniejszy od zera.
4. Wynik jest zwracany jako liczba binarna lub komunikat o błędzie.

## Przykład użycia
```
subtractBinary(1101, 1010)  # Wynik: '11'
subtractBinary(101, 110)    # Wynik: "Nie można odjąć, wynik byłby ujemny."
```

## Kod

### Python
```python
def subtractBinary(a, b):
    # Sprawdzamy, czy oba argumenty są zapisane w systemie binarnym.
    if isBinary(a) and isBinary(b):
        result = ''  # Zmienna przechowująca wynik odejmowania w systemie binarnym.
        borrow = 0  # Zmienna przechowująca pożyczkę (zwykle w przypadku, gdy odjemny bit jest mniejszy od bita odejmowanego).

        # Jeśli a jest mniejsze niż b, to wynik odejmowania będzie ujemny, więc zwracamy komunikat o błędzie.
        if a < b:
            return "Nie można odjąć, wynik byłby ujemny."

        # Pętla wykonuje się, dopóki oba liczby są większe niż 0.
        while a > 0 or b > 0:
            # Dzielimy liczby na pojedyncze bity.
            bit_a = a % 10
            bit_b = b % 10

            # Odejmujemy bity i ewentualnie uwzględniamy pożyczkę.
            sub = bit_a - bit_b - borrow
            # Jeśli wynik odejmowania jest mniejszy niż 0, dodajemy 2 (pożyczka) i ustawiamy borrow na 1.
            if sub < 0:
                sub += 2  
                borrow = 1
            else:
                borrow = 0

            # Dodajemy wynik odejmowania do ciągu, reprezentującego wynik w systemie binarnym.
            result = str(sub) + result

            # Usuwamy ostatni bit z obu liczb.
            a //= 10
            b //= 10

        # Usuwamy wszystkie zera z początku wyniku.
        result = result.lstrip('0')
        # Zwracamy wynik. Jeśli jest pusty, to oznacza, że wynik to 0.
        return result if result else '0'
```

### Ruby
```ruby
def subtractBin(a, b)
  # Sprawdzamy, czy oba argumenty są zapisane w systemie binarnym.
  return "błąd" unless isBinary(a) && isBinary(b)

  result = ''  # Zmienna przechowująca wynik odejmowania w systemie binarnym.
  borrow = 0  # Zmienna przechowująca pożyczkę (zwykle w przypadku, gdy odjemny bit jest mniejszy od bita odejmowanego).

  # Jeśli a jest mniejsze niż b, to wynik odejmowania będzie ujemny, więc zwracamy komunikat o błędzie.
  if a < b
    return "nie można odjąć, wynik byłby ujemny."
  end

  # Pętla wykonuje się, dopóki oba liczby są większe niż 0.
  while a > 0 || b > 0
    # Dzielimy liczby na pojedyncze bity.
    bit_a = a % 10
    bit_b = b % 10

    # Odejmujemy bity i ewentualnie uwzględniamy pożyczkę.
    sub = bit_a - bit_b - borrow

    # Jeśli wynik odejmowania jest mniejszy niż 0, dodajemy 2 (pożyczka) i ustawiamy borrow na 1.
    if sub < 0
      sub += 2
      borrow = 1
    else
      borrow = 0
    end

    # Dodajemy wynik odejmowania do ciągu, reprezentującego wynik w systemie binarnym.
    result = sub.to_s + result
    # Usuwamy ostatni bit z obu liczb.
    a /= 10
    b /= 10
  end

  # Usuwamy wszystkie zera z początku wyniku.
  result = result.sub(/^0+/, '')
  # Zwracamy wynik. Jeśli jest pusty, to oznacza, że wynik to 0.
  return result.empty? ? '0' : result
end
```


## Różnice między Pythonem a Ruby:
1. **Warunek początkowy (sprawdzanie binarności):**
   - W Pythonie używamy `if isBinary(a) and isBinary(b)` do sprawdzenia, czy obie liczby są binarne.
   - W Ruby używamy `return "błąd" unless isBinary(a) && isBinary(b)` do tego samego celu.

2. **Operacja na liczbach:**
   - W Pythonie używamy `a //= 10` i `b //= 10` do dzielenia liczb całkowitych przez 10 (usuwanie ostatniego cyfry).
   - W Ruby używamy `a /= 10` i `b /= 10`, co działa podobnie, ale z inną składnią.

3. **Zwracanie wyniku:**
   - W Pythonie sprawdzamy, czy wynik jest pusty, a następnie usuwamy prowadzące zera za pomocą `result.lstrip('0')`.
   - W Ruby używamy `result.sub(/^0+/, '')` do usunięcia prowadzących zer.

4. **Łączenie cyfr w wynik:**
   - W Pythonie łączymy wynik dodając cyfry za pomocą `result = str(sub) + result`.
   - W Ruby łączymy cyfry w wynik używając `result = sub.to_s + result`.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.



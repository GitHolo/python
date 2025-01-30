# Funkcja Dodawania Liczb Binarnych

## Opis
Funkcja `addBinary` dodaje dwie liczby binarne. Sprawdza, czy podane liczby są binarne, a następnie wykonuje operację dodawania na bitach, uwzględniając przeniesienie.

## Jak działa
1. Funkcja sprawdza, czy obie liczby są liczbami binarnymi, wywołując funkcję `isBinary`.
2. Zaczyna dodawanie bitów, uwzględniając przeniesienie.
3. Kontynuuje dodawanie bitów, dopóki nie przejdzie przez wszystkie bity obu liczb i przeniesienie.
4. Zwraca wynik jako liczbę binarną.

## Przykład użycia
```
addBinary(1101, 1011)  # Wynik: 11000
addBinary(1010, 1100)  # Wynik: 10110
```

## Kod

### Python
```python
def addBinary(a, b):
    # Sprawdzamy, czy obie liczby są w formacie binarnym.
    if isBinary(a) and isBinary(b):
        result = ''  # Inicjalizujemy zmienną 'result', która przechowa wynik.
        carry = 0  # Inicjalizujemy zmienną 'carry', która będzie przechowywać przeniesienie.

        # Pętla wykonuje się, dopóki nie skończą się cyfry w obu liczbach lub nie będzie przeniesienia.
        while a > 0 or b > 0 or carry:
            # Wyciągamy ostatnią cyfrę (bit) z obu liczb.
            bit_a = a % 10
            bit_b = b % 10
            # Obliczamy sumę bitów oraz ewentualne przeniesienie.
            total = bit_a + bit_b + carry
            # Dodajemy wynik do zmiennej 'result' (zachowujemy wynik modulo 2, ponieważ dodajemy bity).
            result = str(total % 2) + result
            # Przechowujemy przeniesienie (dzielenie całkowite przez 2).
            carry = total // 2
            # Usuwamy ostatnią cyfrę z obu liczb.
            a //= 10
            b //= 10
        # Zwracamy wynik.
        return result
```

### Ruby
```ruby
def addBinary(a,b)
  # Sprawdzamy, czy obie liczby są w formacie binarnym.
  return "błąd" unless isBinary(a) && isBinary(b)

  result = ''  # Inicjalizujemy zmienną 'result', która przechowa wynik.
  carry = 0  # Inicjalizujemy zmienną 'carry', która będzie przechowywać przeniesienie.

  # Pętla wykonuje się, dopóki nie skończą się cyfry w obu liczbach lub nie będzie przeniesienia.
  while a > 0 or b > 0 or carry > 0
    # Wyciągamy ostatnią cyfrę (bit) z obu liczb.
    bit_a = a % 10
    bit_b = b % 10
    # Obliczamy sumę bitów oraz ewentualne przeniesienie.
    total = bit_a + bit_b + carry
    # Dodajemy wynik do zmiennej 'result' (zachowujemy wynik modulo 2, ponieważ dodajemy bity).
    result = (total % 2).to_s + result
    # Przechowujemy przeniesienie (dzielenie przez 2).
    carry = total / 2
    # Usuwamy ostatnią cyfrę z obu liczb.
    a /= 10
    b /= 10
  end

  # Zwracamy wynik.
  return result
end
```

## Różnice między Pythonem a Ruby:
1. **Sprawdzanie, czy liczba jest binarna:**
   - W obu językach używamy funkcji `isBinary(a)` oraz `isBinary(b)` do sprawdzenia, czy liczby są binarne, ale w Pythonie nie jest wymagana wcześniejsza konwersja, a w Ruby wykonujemy to przez `to_i`.
   
2. **Zwracanie wartości błędu:**
   - W Pythonie funkcja `addBinary` nie zawiera wbudowanego komunikatu o błędzie, ale zakłada, że liczby będą binarne. Musimy sami sprawdzić, czy są binarne, przed wywołaniem funkcji.
   - W Ruby, jeśli liczba nie jest binarna, zwrócimy "błąd" za pomocą: `return "błąd" unless isBinary(a) && isBinary(b)`.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
# Funkcja Konwersji Liczby Dziesiętnej na Binarna

## Opis
Funkcja `decToBin` konwertuje liczbę dziesiętną na jej reprezentację binarną. Jeśli liczba jest równa zero, funkcja zwróci "0". Funkcja wykonuje konwersję poprzez dzielenie liczby przez 2, zapisując reszty jako kolejne bity liczby binarnej.

## Jak działa
1. Funkcja dzieli liczbę przez 2 i zapisuje resztę z dzielenia (bit) na początku ciągu binarnego.
2. Proces powtarza się, aż liczba osiągnie zero.
3. Funkcja zwraca ciąg binarny, lub "0" jeśli liczba była zerem.

## Przykład użycia
```
decToBin(10)  # Wynik: '1010'
decToBin(0)   # Wynik: '0'
```

## Kod

### [Python](./script.py)
```python
def binToDec(bin: float):
    # Sprawdzamy, czy liczba jest zapisana w systemie binarnym.
    if isBinary(bin):
        # Zamieniamy liczbę na zmiennoprzecinkową, aby móc operować na niej.
        bin = float(bin)
        result = 0  # Zmienna, która przechowa wynik konwersji.
        n = 0  # Zmienna, która będzie reprezentować potęgę liczby 2 (miejsca w systemie binarnym).

        # Pętla wykonuje się, dopóki bin nie stanie się zerem.
        while bin != 0:
            # Sprawdzamy, czy ostatni bit (modulo 10) jest różny od zera.
            if bin % 10 != 0:
                # Dodajemy odpowiednią potęgę liczby 2 do wyniku, jeśli bit jest równy 1.
                result += 2 ** n
            # Usuwamy ostatni bit z liczby bin.
            bin //= 10
            # Zwiększamy wartość potęgi.
            n += 1
        # Zwracamy wynik konwersji z binarnego na dziesiętny.
        return result
```

### [Ruby](./script.rb)
```ruby
def binToDec(bin)
  # Sprawdzamy, czy liczba jest zapisana w systemie binarnym.
  return "błąd" unless isBinary(bin)

  # Konwertujemy liczbę na typ całkowity.
  bin = bin.to_i
  result = 0  # Zmienna, która przechowa wynik konwersji.
  n = 0  # Zmienna, która będzie reprezentować potęgę liczby 2 (miejsca w systemie binarnym).

  # Pętla wykonuje się, dopóki bin nie stanie się zerem.
  while bin != 0
    # Sprawdzamy, czy ostatni bit (modulo 10) jest różny od zera.
    if bin % 10 != 0
      # Dodajemy odpowiednią potęgę liczby 2 do wyniku, jeśli bit jest równy 1.
      result += 2**n
    end
    # Usuwamy ostatni bit z liczby bin.
    bin /= 10
    # Zwiększamy wartość potęgi.
    n += 1
  end

  # Zwracamy wynik konwersji z binarnego na dziesiętny.
  return result
end
```


## Różnice między Pythonem a Ruby:
1. **Łączenie cyfr w wynik:**
   - W Pythonie używamy `binary = str(num % 2) + binary` do połączenia reszty z dzielenia z dotychczasowym wynikiem.
   - W Ruby używamy `binary = (num % 2).to_s + binary`, gdzie reszta z dzielenia jest najpierw konwertowana na string przed połączeniem.



## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
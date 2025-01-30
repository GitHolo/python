# Funkcja Generująca Liczby Szczęśliwe

## Opis
Funkcja `lucky` generuje liczby szczęśliwe w przedziale od 1 do `limit`. Liczby szczęśliwe to liczby, które pozostają w zbiorze po wielokrotnym usuwaniu co drugiej liczby (na początkowym etapie) oraz powtarzaniu tego procesu dla liczb w nowym zbiorze.

## Jak działa
1. Funkcja przyjmuje `limit` jako górny limit zakresu liczb, od 1 do `limit`.
2. Tworzy listę liczb od 1 do `limit`.
3. Iteruje po liście, usuwając liczby, które są wielokrotnością kolejnych liczb w zbiorze (np. w pierwszym kroku usuwamy wszystkie liczby na miejscach parzystych, w kolejnym usuwamy co trzecią liczbę itp.).
4. Proces powtarza się aż do zakończenia iteracji po zbiorze.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może obliczyć liczby szczęśliwe dla określonego limitu:
```
lucky(20)  # [1, 3, 5, 7, 11, <span style="color:red;">13</span>, 17]
```

## Kod

### [Python](./script.py)
```python
def lucky(limit):
    arr = list(range(1, limit + 1))  # Tworzymy listę liczb od 1 do limitu
    n = 1  # Inicjalizujemy licznik

    while n < len(arr):
        step = arr[n]  # Pobieramy liczbę na miejscu n
        arr = [num for i, num in enumerate(arr) if (i + 1) % step != 0]  # Usuwamy liczby będące wielokrotnością 'step'
        n += 1  # Zwiększamy licznik

    return arr  # Zwracamy listę liczb szczęśliwych
```

### [Ruby](./script.rb)
```ruby
def lucky(limit)
  arr = (1..limit).to_a  # Tworzymy listę liczb od 1 do limitu
  n = 1  # Inicjalizujemy licznik

  while n < arr.length
    step = arr[n]  # Pobieramy liczbę na miejscu n
    arr = arr.each_with_index.reject { |num, i| (i + 1) % step == 0 }.map(&:first)  # Usuwamy liczby będące wielokrotnością 'step'
    n += 1  # Zwiększamy licznik
  end

  return arr  # Zwracamy listę liczb szczęśliwych
end
```

## Różnice między Pythonem a Ruby:
1. **Tworzenie listy liczb od 1 do limitu:**
   - W Pythonie używamy `arr = list(range(1, limit + 1))` do stworzenia listy liczb.
   - W Ruby tworzymy listę za pomocą `arr = (1..limit).to_a`.

2. **Iterowanie przez listę:**
   - W Pythonie korzystamy z `enumerate(arr)` do uzyskania indeksu i elementu podczas iteracji, a następnie filtrujemy elementy za pomocą list comprehension.
   - W Ruby używamy `each_with_index` do iterowania po elementach z indeksami, a następnie stosujemy `reject` do usunięcia elementów, które spełniają warunek, a na końcu `map(&:first)` w celu uzyskania wartości.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.

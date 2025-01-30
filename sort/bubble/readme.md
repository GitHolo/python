# Algorytm Sortowania Bąbelkowego (BubbleSort)

## Opis
Algorytm sortowania bąbelkowego (Bubble Sort) to jeden z najprostszych algorytmów sortujących. Działa on poprzez iterowanie po tablicy, porównywanie sąsiednich elementów i zamienianie ich miejscami, jeśli są w złej kolejności. Proces ten powtarza się aż do momentu, gdy tablica jest w pełni posortowana.

## Jak działa
1. Funkcja `bubble` przyjmuje tablicę `arr` jako argument.
2. Algorytm przechodzi przez tablicę, porównując pary sąsiednich elementów.
3. Jeśli elementy są w złej kolejności, zamienia je miejscami.
4. Jeśli podczas pełnej iteracji nie dokonano żadnej zamiany, algorytm kończy działanie, uznając tablicę za posortowaną.
5. Algorytm zwraca posortowaną tablicę.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może dostarczyć tablicę liczb:
```
arr = [64, 34, 25, 12, 22, 11, 90]
```
Wynik działania skryptu:
```
[11, 12, 22, 25, 34, 64, 90]
```

## Kod

### [Python](./script.py)
```python
def bubble(arr: list):
    n = len(arr)  # Ustala długość tablicy
    
    for i in range(n):  # Iteruje po tablicy
        swapped = False  # Flaga, która sprawdza, czy dokonano zamiany

        for j in range(0, n-i-1):  # Porównuje sąsiednie elementy
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Zamiana miejscami
                swapped = True  # Ustawia flagę na True

        if (swapped == False):  # Jeśli nie dokonano żadnej zamiany, kończy działanie
            break

    return arr  # Zwraca posortowaną tablicę
```

### [Ruby](./script.rb)
```ruby
def bubbleSort(arr)
  n = arr.length  # Ustala długość tablicy

  n.times do |i|  # Iteruje po tablicy
    swapped = false  # Flaga, która sprawdza, czy dokonano zamiany

    (0...(n-i-1)).each do |j|  # Porównuje sąsiednie elementy
      if arr[j] > arr [j+1]
        arr[j], arr[j+1] = arr[j+1], arr[j]  # Zamiana miejscami
        swapped = true  # Ustawia flagę na True
      end
    end

    break if swapped == false  # Jeśli nie dokonano żadnej zamiany, kończy działanie
  end

  return arr  # Zwraca posortowaną tablicę
end
```

## Różnice między Pythonem a Ruby:
1. **Pętla `for`/`times`:**
   - W Pythonie używamy pętli `for` z zakresem `range(n)` do iterowania przez wszystkie elementy tablicy.
   - W Ruby używamy metody `times` do wykonania pętli `n` razy, co jest idiomatycznym sposobem iteracji.

2. **Zakres pętli wewnętrznej:**
   - W Pythonie wewnętrzna pętla jest zapisana jako `for j in range(0, n-i-1)`, co oznacza iterację od `0` do `n-i-1`.
   - W Ruby używamy zapisu `(0...(n-i-1)).each do |j|`, gdzie zakres jest nieco bardziej idiomatyczny, z wykorzystaniem operatora `...` (zakres bez ostatniego elementu).

3. **Zmienna `swapped`:**
   - W Pythonie flaga `swapped` jest inicjowana jako `False`, a po każdej zamianie ustawiana na `True`. Jeśli po jednej pełnej iteracji nie zostaną dokonane żadne zamiany, pętla główna zostaje zakończona.
   - W Ruby działa to w identyczny sposób, jednak składnia Ruby umożliwia zastosowanie konstrukcji `break` do przerwania pętli, co jest bardziej naturalne w tym języku.


4. **Składnia nawiasów:**
   - W Pythonie nawiasy są wymagane dla funkcji i metod, takich jak `range(n)` i `arr[j]`.
   - W Ruby nawiasy są opcjonalne przy metodach, takich jak `arr.length` i `arr[j]`.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
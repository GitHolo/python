# Algorytm Sortowania QuickSort

## Opis
Ten skrypt implementuje algorytm sortowania QuickSort, który jest jednym z najpopularniejszych algorytmów sortujących. Działa on na zasadzie "divide-and-conquer", wybierając element zwany "pivotem" i dzieląc tablicę na dwie części, które następnie są rekurencyjnie sortowane.

## Jak działa
1. Funkcja `quickSort` przyjmuje trzy argumenty: tablicę `arr`, oraz dwa indeksy: `low` i `high`, które definiują zakres sortowania.
2. Funkcja `partition` wybiera element pivot (w tym przypadku ostatni element tablicy), a następnie dzieli tablicę na dwie części:
   - Lewa część zawiera elementy mniejsze lub równe pivotowi.
   - Prawa część zawiera elementy większe od pivota.
3. Tablica jest sortowana rekurencyjnie poprzez wywołania `quickSort` na lewą i prawą część tablicy.
4. Funkcja zwraca posortowaną tablicę.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może dostarczyć tablicę liczb:
```
arr = [10, 7, 8, 9, 1, 5]
```
Wynik działania skryptu:
```
[1, 5, 7, 8, 9, 10]
```

## Kod

### [Python](./script.py)
```python
def quickSort(arr: list, low=0, high=None):
    if high is None:
        high = len(arr)-1  # Ustala wartość 'high' jako ostatni indeks tablicy
    
    if low < high:
        pivot = partition(arr, low, high)  # Wywołuje funkcję partition, aby znaleźć indeks pivota
        quickSort(arr, low, pivot-1)  # Rekurencyjne wywołanie dla lewej części
        quickSort(arr, pivot+1, high)  # Rekurencyjne wywołanie dla prawej części
    
    return arr  # Zwraca posortowaną tablicę

def partition(arr: list, low, high):
    pivot = arr[high]  # Wybiera ostatni element tablicy jako pivot
    i = low - 1  # Ustala indeks dla mniejszej części tablicy

    for j in range(low, high):  # Iteruje po tablicy od 'low' do 'high'
        if arr[j] <= pivot:  # Jeśli element jest mniejszy lub równy pivotowi
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Zamienia elementy

    arr[i+1], arr[high] = arr[high], arr[i+1]  # Umieszcza pivot na odpowiedniej pozycji
    return i+1  # Zwraca indeks pivota
```

### [Ruby](./script.rb)
```ruby
def quickSort(arr, low = 0, high = nil)
  if high == nil
    high = arr.length - 1  # Ustala wartość 'high' jako ostatni indeks tablicy
  end

  if low < high
    pivot = partition(arr, low, high)  # Wywołuje funkcję partition, aby znaleźć indeks pivota
    quickSort(arr, low, pivot - 1)  # Rekurencyjne wywołanie dla lewej części
    quickSort(arr, pivot + 1, high)  # Rekurencyjne wywołanie dla prawej części
  end

  return arr  # Zwraca posortowaną tablicę
end

def partition(arr, low, high)
  pivot = arr[high]  # Wybiera ostatni element tablicy jako pivot
  i = low - 1  # Ustala indeks dla mniejszej części tablicy

  (low..high-1).each do |j|  # Iteruje po tablicy od 'low' do 'high-1'
    if arr[j] <= pivot  # Jeśli element jest mniejszy lub równy pivotowi
      i += 1
      arr[i], arr[j] = arr[j], arr[i]  # Zamienia elementy
    end
  end

  arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Umieszcza pivot na odpowiedniej pozycji
  return i + 1  # Zwraca indeks pivota
end
```

## Różnice między Pythonem a Ruby:
1. **Domyślne wartości argumentów:**
   - W Pythonie wartość domyślna dla `high` jest ustawiana na `None` i obliczana wewnątrz funkcji jako `len(arr)-1`.
   - W Ruby wartość domyślna dla `high` jest ustawiana na `nil` i obliczana podobnie, ale bezpośrednio w kodzie.

2. **Pętla `for` i `each`:**
   - W Pythonie do iteracji po elementach tablicy używamy pętli `for`, która iteruje po indeksach.
   - W Ruby używamy metody `each` do iteracji po zakresie `(low..high-1)`.

3. **Indeksowanie tablicy:**
   - W Pythonie indeksy są używane bezpośrednio, np. `arr[i]`, `arr[j]`.
   - W Ruby indeksowanie tablicy również działa w podobny sposób, ale wykorzystuje metodę `each` oraz zakresy.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
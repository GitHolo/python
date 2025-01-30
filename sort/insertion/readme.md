# Algorytm Sortowania przez Wstawianie (InsertSort)

## Opis
Ten skrypt implementuje algorytm sortowania przez wstawianie (Insert Sort), który działa poprzez iterowanie po tablicy i wstawianie każdego elementu w odpowiednie miejsce w posortowanej części tablicy.

## Jak działa
1. Funkcja `insertSort` przyjmuje jedną tablicę `arr` jako argument.
2. Algorytm przechodzi przez tablicę od drugiego elementu (`i = 1`) do ostatniego elementu.
3. Dla każdego elementu (tzw. `key`) znajduje odpowiednie miejsce w posortowanej części tablicy (wszystkie elementy przed `i`).
4. Przesuwa większe elementy o jedno miejsce w prawo, aby zrobić miejsce dla `key`.
5. Algorytm zwraca posortowaną tablicę.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może dostarczyć tablicę liczb:
```
arr = [12, 11, 13, 5, 6]
```
Wynik działania skryptu:
```
[5, 6, 11, 12, 13]
```

## Kod

### Python
```python
def insertSort(arr: list):
    for i in range(1, len(arr)):  # Iteruje po tablicy zaczynając od drugiego elementu
        key = arr[i]  # Element, który będzie wstawiany w odpowiednie miejsce
        j = i - 1  # Indeks dla porównania z elementami po lewej stronie
        
        # Przesuwa elementy większe od 'key' o jedno miejsce w prawo
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Wstawia 'key' w odpowiednie miejsce
        arr[j + 1] = key

    return arr  # Zwraca posortowaną tablicę
```

### Ruby
```ruby
def insertSort(arr)
  for i in 1...(arr.length)  # Iteruje po tablicy zaczynając od drugiego elementu
    key = arr[i]  # Element, który będzie wstawiany w odpowiednie miejsce
    j = i - 1  # Indeks dla porównania z elementami po lewej stronie
    
    # Przesuwa elementy większe od 'key' o jedno miejsce w prawo
    while j >= 0 and arr[j] > key
      arr[j+1] = arr[j]
      j -= 1
    end
    
    # Wstawia 'key' w odpowiednie miejsce
    arr[j + 1] = key
  end

  return arr  # Zwraca posortowaną tablicę
end
```

## Różnice między Pythonem a Ruby:
1. **Pętla `for`:**
   - W Pythonie używamy pętli `for` z zakresem `range(1, len(arr))` do iteracji po elementach tablicy od drugiego elementu.
   - W Ruby używamy pętli `for i in 1...(arr.length)` do iteracji, gdzie zakres `1...arr.length` oznacza iterację od 1 do `arr.length - 1`.

2. **Indeksowanie tablicy:**
   - W obu językach indeksowanie tablicy działa w podobny sposób, np. `arr[i]` w Pythonie i Ruby.

3. **Wstawianie elementu:**
   - W Pythonie wstawianie elementu do posortowanej części tablicy odbywa się poprzez przypisanie `arr[j + 1] = key`.
   - W Ruby działa to w ten sam sposób, ale z różnicą w składni, gdzie nie ma nawiasów w przypisaniu.

4. **Pętla `while`:**
   - W Pythonie warunek w pętli `while` jest zapisany jako `while j >= 0 and arr[j] > key`.
   - W Ruby zapis jest identyczny, ale używamy słowa kluczowego `and` zamiast `&&`, co jest bardziej idiomatyczne w Ruby.

5. **Zwracanie wartości:**
   - W Pythonie `insertSort` zwraca posortowaną tablicę `arr`.
   - W Ruby, podobnie jak w Pythonie, funkcja `insertSort` zwraca posortowaną tablicę, a `return` jest używane w tej samej formie.

6. **Brak nawiasów przy metodach:**
   - W Pythonie musimy używać nawiasów przy metodach, np. `len(arr)`.
   - W Ruby metody takie jak `arr.length` są używane bez nawiasów, co jest jednym z różnic w składni obu języków.

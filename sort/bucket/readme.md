# Algorytm Sortowania przez Kubełki (BucketSort)

## Opis
Ten skrypt implementuje algorytm sortowania przez kubełki (Bucket Sort), który jest algorytmem sortującym opartym na podziale danych na mniejsze grupy, tzw. kubełki. Następnie każdy kubełek jest sortowany (zwykle za pomocą innego algorytmu sortowania) i łączony z powrotem, aby uzyskać posortowaną tablicę.

## Jak działa
1. Funkcja `bucketSort` przyjmuje tablicę `arr` jako argument.
2. Tablica jest dzielona na `n` kubełków (gdzie `n` to długość tablicy).
3. Każdy element tablicy jest przyporządkowywany do odpowiedniego kubełka.
4. Każdy kubełek jest sortowany za pomocą algorytmu sortowania przez wstawianie (Insert Sort).
5. Na końcu elementy z wszystkich kubełków są łączone w jedną posortowaną tablicę.

## Przykład użycia
Po uruchomieniu skryptu użytkownik może dostarczyć tablicę liczb:
```
arr = [0.42, 0.32, 0.23, 0.55, 0.31, 0.12]
```
Wynik działania skryptu:
```
[0.12, 0.23, 0.31, 0.32, 0.42, 0.55]
```

## Kod

### Python
```python
def bucketSort(arr: list):
    n = len(arr)  # Ustala długość tablicy
    buckets = [[] for _ in range(n)]  # Tworzy n pustych kubełków

    for num in arr:  # Rozdziela elementy do kubełków
        bi = int(n * num)  # Oblicza indeks kubełka na podstawie wartości
        buckets[bi].append(num)  # Dodaje element do odpowiedniego kubełka
    
    for bucket in buckets:  # Sortuje każdy kubełek (z użyciem insertSort)
        insertSort(bucket)

    index = 0
    for bucket in buckets:  # Łączy elementy z kubełków z powrotem do tablicy
        for num in bucket:
            arr[index] = num
            index += 1
```

### Ruby
```ruby
def bucketSort(arr)
  n = arr.length  # Ustala długość tablicy
  buckets = Array.new(n) { [] }  # Tworzy n pustych kubełków

  arr.each do |num|  # Rozdziela elementy do kubełków
    bi = n * num  # Oblicza indeks kubełka na podstawie wartości
    buckets[bi] << num  # Dodaje element do odpowiedniego kubełka
  end

  buckets.each do |bucket|  # Sortuje każdy kubełek (z użyciem insertSort)
    insertSort(bucket)
  end

  index = 0
  buckets.each do |bucket|  # Łączy elementy z kubełków z powrotem do tablicy
    bucket.each do |num|
      arr[index] = num
      index += 1
    end
  end
end
```

## Różnice między Pythonem a Ruby:
1. **Tworzenie kubełków:**
   - W Pythonie kubełki są tworzone za pomocą listy: `buckets = [[] for _ in range(n)]`.
   - W Ruby kubełki są tworzone przy pomocy metody `Array.new(n) { [] }`, co tworzy tablicę z `n` pustymi tablicami.

2. **Iteracja po tablicy:**
   - W Pythonie iteracja po tablicy `arr` odbywa się za pomocą pętli `for num in arr`.
   - W Ruby używa się metody `each`, czyli `arr.each do |num|`.

3. **Obliczanie indeksu kubełka:**
   - W Pythonie obliczamy indeks kubełka za pomocą: `bi = int(n * num)`, gdzie `num` jest elementem tablicy.
   - W Ruby robimy to w identyczny sposób: `bi = n * num`, ale Ruby automatycznie konwertuje wartości zmiennoprzecinkowe, co może prowadzić do nieco innych zachowań w przypadku dużych liczb.

4. **Dodawanie elementów do kubełków:**
   - W Pythonie używamy metody `append()` do dodawania elementów do kubełka, np. `buckets[bi].append(num)`.
   - W Ruby używamy operatora `<<`, np. `buckets[bi] << num`.

5. **Sortowanie kubełków:**
   - W Pythonie każdemu kubełkowi przypisujemy funkcję `insertSort(bucket)` w celu posortowania.
   - W Ruby robimy to w ten sam sposób, wywołując `insertSort(bucket)` na każdym kubełku.

6. **Łączenie elementów z kubełków:**
   - W Pythonie łączymy posortowane elementy z kubełków z powrotem do tablicy, używając `arr[index] = num`.
   - W Ruby łączymy je w identyczny sposób, również używając `arr[index] = num`.

7. **Różnice w składni:**
   - Python używa nawiasów kwadratowych do indeksowania list, np. `arr[i]`.
   - Ruby używa tego samego zapisu, ale składnia Ruby jest bardziej zwarta i pozwala na używanie metod bez nawiasów w wielu przypadkach.

8. **Typy zmiennych:**
   - W Pythonie zmienne są typowane dynamicznie, ale muszą być odpowiednio przekształcone (np. `int(n * num)`).
   - W Ruby również zmienne są dynamicznie typowane, ale automatyczne konwersje są nieco bardziej elastyczne.

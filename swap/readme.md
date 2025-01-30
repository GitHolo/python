# Funkcja Zamiany Wartości (Swap)

## Opis
Ten skrypt demonstruje funkcję `swap`, która zamienia wartości dwóch zmiennych i modyfikuje ich zawartość, dodając tekst opisujący zmienione wartości. 

## Jak działa
1. Użytkownik podaje dwie wartości wejściowe: `a` i `b`.
2. Funkcja `swap` zamienia wartości `a` i `b` miejscami.
3. Po zamianie do każdej zmiennej dodawany jest tekst opisowy:
   - `a` staje się `"a is ..."` z wartością poprzedniej zmiennej `b`.
   - `b` staje się `"b is ..."` z wartością poprzedniej zmiennej `a`.
4. Funkcja zwraca dwie zmodyfikowane wartości.
5. Wynik jest wyświetlany na ekranie.

## Przykład użycia
Po uruchomieniu skryptu użytkownik zostanie poproszony o podanie wartości:
```
a: Hello
b: World
```
Wynik działania skryptu:
```
('a is World', 'b is Hello')
```

## Kod

### Python
```python
def swap(a, b):
    a, b = b, a
    a = "a is " + str(a)
    b = "b is " + str(b)
    return a, b

a = input('a: ')
b = input('b: ')

print(swap(a, b))
```
### Ruby
```ruby
def swap(a, b)
  a, b = b, a
  a = "a is #{a}"
  b = "b is #{b}"
  return a,b
end

print "a: "
a = gets.chomp
print "b: "
b = gets.chomp

print swap(a, b)
```

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

### [Python](./script.py)
```python
def swap(a, b):
    a, b = b, a  # Zamienia miejscami wartości a i b
    a = "a is " + str(a)  # Konwertuje 'a' na string i dodaje etykietę
    b = "b is " + str(b)  # Konwertuje 'b' na string i dodaje etykietę
    return a, b  # Zwraca zaktualizowane 'a' i 'b' z etykietami

a = input('a: ')  # Pobiera dane wejściowe od użytkownika dla 'a'
b = input('b: ')  # Pobiera dane wejściowe od użytkownika dla 'b'

print(swap(a, b))  # Drukuje zamienione wartości z etykietami
```

### [Ruby](./script.rb)
```ruby
def swap(a, b)
  a, b = b, a  # Zamienia miejscami wartości a i b
  a = "a is #{a}"  # Używa interpolacji stringów, aby dodać etykietę do 'a'
  b = "b is #{b}"  # Używa interpolacji stringów, aby dodać etykietę do 'b'
  return a,b  # Zwraca zaktualizowane 'a' i 'b' z etykietami
end

print "a: "  # Wypisuje komunikat przed pobraniem danych wejściowych
a = gets.chomp  # Pobiera dane wejściowe dla 'a'
print "b: "  # Wypisuje komunikat przed pobraniem danych wejściowych
b = gets.chomp  # Pobiera dane wejściowe dla 'b'

print swap(a, b)  # Drukuje zamienione wartości z etykietami
```

## Różnice między Pythonem a Ruby:
1. **Wejście/Wyjście:**
   - W Pythonie do pobierania danych wejściowych używamy funkcji `input()`, która zawsze zwraca dane w formie stringa.
   - W Ruby używamy `gets.chomp` do pobierania danych wejściowych, a metoda `chomp` usuwa znak nowej linii.

2. **Łączenie stringów:**
   - W Pythonie łączymy stringi za pomocą operatora `+` (`"a is " + str(a)`).
   - W Ruby używamy interpolacji stringów z użyciem `#{}` do wstawiania zmiennych bezpośrednio do ciągów znaków (`"a is #{a}"`).

3. **Definicja funkcji:**
   - W obu językach używamy słowa kluczowego `def` do definiowania funkcji, ale Python używa wcięć do określenia zakresu, natomiast Ruby używa słowa kluczowego `end` do zamknięcia definicji funkcji.

4. **Zasięg zmiennych i zwracanie wartości:**
   - W obu językach możemy zamienić miejscami wartości zmiennych, a potem je zwrócić. Ruby używa `return a, b`, co jest podobne do zwracania krotek w Pythonie (`return a, b`).

5. **Komunikaty przed pobieraniem danych wejściowych:**
   - W Pythonie komunikaty dla użytkownika są podawane w funkcji `input()`.
   - W Ruby komunikaty są wypisywane przed wywołaniem `gets.chomp`, za pomocą funkcji `print`.

## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
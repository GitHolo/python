# Funkcja Wypełniania Tablicy

## Opis
Funkcja `arrFill` pozwala na wypełnienie tablicy liczbami, które użytkownik wprowadza z klawiatury. Program najpierw prosi o ilość liczb, a następnie o każdą z nich, którą dodaje do tablicy.

## Jak działa
1. Funkcja prosi użytkownika o podanie liczby elementów, które mają zostać wprowadzone do tablicy.
2. W pętli użytkownik wprowadza liczby, które są dodawane do tablicy.
3. Proces trwa do momentu, aż użytkownik poda wszystkie liczby.

## Przykład użycia
```
arrFill(arr)  # Użytkownik wprowadza liczby, które są dodawane do tablicy `arr`.
```

## Kod


### [Python](./script.py)
```python
def arrFill(arr: list):
    # Pobieramy liczbę 'n', która określa ile liczb ma zostać wprowadzonych do tabeli.
    n = int(input("podaj ilość liczb w tabeli: "))
    # Pętla wykonuje się, dopóki nie wprowadzimy wszystkich liczb.
    while n > 0:
        # Pobieramy pojedynczą liczbę 'a' i dodajemy ją do listy 'arr'.
        a = int(input("podaj liczbe: "))
        arr.append(a)  # Dodajemy liczbę do listy.
        n -= 1  # Zmniejszamy licznik 'n' o 1.
    # Zwracamy wypełnioną listę 'arr'.
    return arr
```

### Ruby
```ruby
def arrFill(arr)
  # Wyświetlamy prośbę o podanie liczby elementów w tabeli.
  print "podaj ilość liczb w tabeli: "
  # Odczytujemy liczbę elementów, które mają być wprowadzone do tabeli.
  n = gets.chomp.to_i

  # Pętla wykonuje się, dopóki nie wprowadzimy wszystkich liczb.
  while n > 0
    # Wyświetlamy prośbę o podanie jednej liczby.
    print "podaj liczbe: "
    # Odczytujemy liczbę 'a' i dodajemy ją do tablicy 'arr'.
    a = gets.chomp.to_i
    arr << a  # Dodajemy liczbę do tablicy.
    n -= 1  # Zmniejszamy licznik 'n' o 1.
  end

  # Zwracamy wypełnioną tablicę 'arr'.
  return arr
end
```

## Różnice między Pythonem a Ruby:
1. **Prośba o wejście od użytkownika:**
   - W Pythonie używamy funkcji `input()` do pobierania danych od użytkownika. Wynik jest zawsze ciągiem znaków, dlatego konwertujemy go na liczbę całkowitą za pomocą `int()`.
   - W Ruby używamy `gets.chomp` do pobrania wejścia, a następnie konwertujemy je na liczbę całkowitą za pomocą `.to_i`.

2. **Dodawanie elementów do tablicy:**
   - W Pythonie używamy metody `append()` do dodawania elementów do listy.
   - W Ruby używamy operatora `<<`, który działa podobnie do `append()` w Pythonie, dodając element do tablicy.

3. **Drukowanie komunikatów:**
   - W Pythonie do wyświetlania komunikatów używamy funkcji `input()`, która jednocześnie wyświetla tekst i pobiera dane.
   - W Ruby używamy `print` do wypisania tekstu przed pobraniem danych, ale nie jest to połączone z pobieraniem danych.


## Jak uruchomić?
1. Uruchom plik Python.
2. Wprowadź liczbę całkowitą w odpowiedzi na pytanie.
2. Otrzymasz wynik w konsoli.
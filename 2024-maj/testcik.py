from collections import Counter

liczba = 11
czynniki = []
while liczba % 2 == 0:
    czynniki.append(2)
    liczba //= 2

for i in range(3, int(liczba**0.5)+1, 2):
    while liczba % i == 0:
        czynniki.append(i)
        liczba //= i

if liczba > 2:
    czynniki.append(liczba)

print(czynniki)

one = [2, 3, 4, 5, 6, 7, 7, 7, 2, 3, 4, 5, 6]
counter = Counter(one)
print(counter.items())
print(counter)
print(one)

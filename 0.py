n = int(input("Podaj a: \n"))
b = 1
c = 0
d = 0
while n > 0:
    a = n % 10
    n = n // 10
    if a % 2 == 0:
        c = c + b * (a // 2)
    else:
        c = c + b
        d+=1
    b = b * 10
print("Wynik:", c)
print("Liczba wykonań instrukcji c = c + b: ",d)
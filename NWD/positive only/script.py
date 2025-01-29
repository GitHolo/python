def nwd(a,b):
    if a>0 and b>0:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    else:
        return "błąd"

a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))
print(str(nwd(a,b)))
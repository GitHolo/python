def euclideanNWD(a,b):
    while b!=0:
        r=a%b
        a,b=b,r
    return a

a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))
print(euclideanNWD(a,b))
def decToBin(num: int):
    
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    return binary or 0

num = int(input("Podaj liczbę dziesiętną: "))
print(f"Liczba binarna: {decToBin(num)}")

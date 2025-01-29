def decToBin(num: float):
    
    factor = 1
    while num != int(num):
        num *= 2
        factor *= 2

    num = int(num)
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    binary += '0' * (factor - 1)

    return binary

# Example usage
num = float(input("Podaj liczbę dziesiętną: "))
print(f"Liczba binarna: {decToBin(num)}")

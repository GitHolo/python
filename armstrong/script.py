def armstrong(num: int):
    factor = 0
    result = 0
    while result < num:
        result = sum(int(digit) ** factor for digit in str(num))
        factor+=1
        if result == num:
            return True
    return False

num = int(input("Podaj liczbę: "))
print(armstrong(num))

def isBinary(n: int):
    for i in str(n):
        if i not in ['0', '1']:
            return False
    return True

def subtractBinary(a, b):
    if isBinary(a) and isBinary(b):
        result = ''
        borrow = 0

        if a < b:
            return "Nie można odjąć, wynik byłby ujemny."

        while a > 0 or b > 0:
            bit_a = a % 10
            bit_b = b % 10

            sub = bit_a - bit_b - borrow
            if sub < 0:
                sub += 2  
                borrow = 1
            else:
                borrow = 0

            result = str(sub) + result

            a //= 10
            b //= 10

        result = result.lstrip('0')
        return result if result else '0'

a = int(input("Podaj liczbę a w systemie binarnym: "))
b = int(input("Podaj liczbę b w systemie binarnym: "))

print(f"Wynik odejmowania: {subtractBinary(a, b)}")

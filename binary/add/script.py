def isBinary(n: int):

    for i in str(n):

        if str(i) not in ['0', '1']:

            return False
        
    return True

def addBinary(a, b):

    if isBinary(a) and isBinary(b):

        result = ''
        carry = 0
    
        while a > 0 or b > 0 or carry:

            bit_a = a % 10
            bit_b = b % 10
            
            total = bit_a + bit_b + carry
            
            result = str(total % 2) + result
            
            carry = total // 2
            
            a //= 10
            b //= 10
    
        return result
        

        

a = int(input("Podaj liczbę a w systemie binarnym: "))
b = int(input("Podaj liczbę b w systemie binarnym: "))

print(addBinary(a, b))
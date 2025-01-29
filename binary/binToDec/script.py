def isBinary(n: int):
    for i in str(n):
        if str(i) not in ['0', '1']:
            return False
    return True

def binToDec(bin: float):

    if isBinary(bin):

        bin = float(bin)
        result = 0
        n = 0

        while bin != 0:

            if bin%10!=0:

                result+=2**n

            bin//=10
            n+=1
            
        return result

num = input("podaj liczbę binarną: ")
print(binToDec(num))





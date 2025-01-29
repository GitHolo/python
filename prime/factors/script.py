import math

def divisor(a):
    result = []
    while a%2==0:
        result.append(2)
        a//=2
    for i in range(3, int(math.sqrt(a))+1, 2):
        while a%i==0:
            result.append(i)
            a//=i
    if a>1:
        result.append(a)
    return result
  

a = int(input("Wpisz liczbę: "))
print("dzielniki liczby: "+str(divisor(a)))      
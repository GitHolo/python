def isPrime(n):

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:

            return False
        
    return True


def primeGen(max):

    primes = []
    num = 2
    
    while max >0:

        if isPrime(num):

            primes.append(num)
            max-=1
        num+=1

    return primes

max = int(input("podaj limit: "))
print(primeGen(max))
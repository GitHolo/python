def isPrime(n)

  (2...(n**0.5)+1).each do |i|

    if n % i == 0

      return false

    end

  end

  return true

end

def primeGen(max)
  primes = []
  num = 2

  while max > 0
    if isPrime(num)
      primes.append(num)
      max-=1
    end
    num+=1

  end

  return primes

end

print "podaj limit: "
max = gets.chomp.to_i

print primeGen(max)

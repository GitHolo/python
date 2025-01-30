def isPrime(n)

  (2...(n**0.5)+1).each do |i|

    if n % i == 0

      return false

    end

  end

  return true

end

n = 12

print isPrime(n)

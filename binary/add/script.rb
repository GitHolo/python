def isBinary(n)

  n.to_s.each_char do |i|

    if !['0', '1'].include?(i.to_s)

      return false

    end
  end

  return true

end

def addBinary(a,b)

  return "błąd" unless isBinary(a) && isBinary(b)

  result = ''
  carry = 0

  while a > 0 or b > 0 or carry > 0

    bit_a = a % 10
    bit_b = b % 10

    total = bit_a + bit_b + carry

    result = (total % 2).to_s + result

    carry = total / 2

    a/=10
    b/=10

  end

  return result

end

print "Podaj liczbę a w systemie binarnym: "
a = gets.chomp.to_i
print "Podaj liczbę b w systemie binarnym: "
b = gets.chomp.to_i
puts addBinary(a, b)

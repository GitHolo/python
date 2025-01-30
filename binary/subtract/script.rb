def isBinary(n)
  n.to_s.each_char do |i|
    return false unless ['0', '1'].include?(i)
  end
  return true
end

def subtractBin(a, b)
  return "błąd" unless isBinary(a) && isBinary(b)

  result = ''
  borrow = 0

  if a < b
    return "nie można odjąć, wynik byłby ujemny."
  end

  while a > 0 || b > 0
    bit_a = a % 10
    bit_b = b % 10

    sub = bit_a - bit_b - borrow

    if sub < 0
      sub += 2
      borrow = 1
    else
      borrow = 0
    end

    result = sub.to_s + result
    a /= 10
    b /= 10
  end

  result = result.sub(/^0+/, '')
  return result.empty? ? '0' : result
end

print "Podaj liczbę a w systemie binarnym: "
a = gets.chomp.to_i
print "Podaj liczbę b w systemie binarnym: "
b = gets.chomp.to_i
puts subtractBin(a, b)

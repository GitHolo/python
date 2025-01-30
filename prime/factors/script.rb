def divisor(a)
  result = []
  while a%2 == 0
    result << 2
    a/=2
  end
  (3..Math.sqrt(a)+1.to_i).step(2) do |i|
    while a%i == 0
      result << i.to_i
      a/=i
    end
  end
  if a>1
    result << a.to_i
  end
  return result
end


print "wypisz liczbę: "
a = gets.chomp.to_i

print "dzielniki liczby: ", divisor(a)

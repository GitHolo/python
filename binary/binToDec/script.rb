def isBinary(n)

  n.to_s.each_char do |i|

    if !['0', '1'].include?(i.to_s)

      return false

    end
  end

  return true

end

def binToDec(bin)
  return "błąd" unless isBinary(bin)

  bin = bin.to_i
  result = 0
  n = 0

  while bin != 0
    if bin % 10 != 0
      result += 2**n
    end
    bin /= 10
    n += 1
  end


  return result


end

print "podaj liczbę binarną: "
num = gets.chomp
print(binToDec(num))

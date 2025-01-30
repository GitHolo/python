def decToBin(num)

  binary = ''

  while num > 0

    binary = (num%2).to_s + binary
    num /=2

  end
  return binary || '0'
end

print "podaj liczbę dziesiętną: "
num = gets.chomp.to_i
print(decToBin(num))

def armstrong(num)
  factor = 0
  result = 0
  while result < num
    result = num.to_s.chars.map { |digit| digit.to_i ** factor }.sum
    factor+=1
    return true if result == num
  end
  return false
end

puts(armstrong(153))

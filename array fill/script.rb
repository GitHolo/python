def arrFill(arr)

  print "podaj ilość liczb w tabeli: "
  n = gets.chomp.to_i

  while n>0
    print "podaj liczbe: "
    a = gets.chomp.to_i
    arr << a
    n-=1
  end

  return arr

end


arr = []

print arrFill(arr)

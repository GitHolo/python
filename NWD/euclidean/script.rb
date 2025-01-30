def euclideanNWD(a,b)
  while b!=0
    r=a%b
    a,b=b,r
  end
  return a
end

print "podaj liczbę a: "
a = gets.chomp.to_i
print "podaj liczbę b: "
b = gets.chomp.to_i
print euclideanNWD(a,b)

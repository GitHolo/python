def nwd(a,b)
  if a>0 && b>0
    while a != b
      if a > b
        a-=b
      else
        b-=a
      end
    end
    return a
  else return "błąd"
  end
end

print "podaj liczbę a: "
a = gets.chomp.to_i
print "podaj liczbę b: "
b = gets.chomp.to_i
print nwd(a,b)

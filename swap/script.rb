def swap(a, b)
  a, b = b, a
  a = "a is #{a}"
  b = "b is #{b}"
  return a,b
end

print "a: "
a = gets.chomp
print "b: "
b = gets.chomp

print swap(a, b)

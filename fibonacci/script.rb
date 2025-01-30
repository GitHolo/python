def fibonacci(max)
  result = [0]
  first = result[0]
  second = first+1

  while max>0
    first, second = second, first+second
    result << first
    max-=1
  end
  return result
end

print fibonacci(19)

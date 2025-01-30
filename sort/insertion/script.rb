def insertSort(arr)

  for i in 1...(arr.length)
    key = arr[i]
    j = i - 1

    while j >=0 and arr[j] > key
      arr[j+1] = arr[j]
      j-=1
    end
    arr [j+1] = key

  end

  return arr

end

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

print arrFill(arr), "\n"

print insertSort(arr)

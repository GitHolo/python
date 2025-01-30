def bubbleSort(arr)
  n = arr.length

  n.times do |i|
    swapped = false

    (0...(n-i-1)).each do |j|
      if arr[j] > arr [j+1]
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = true
      end

    end

    break if swapped == false

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

print arrFill(arr),"\n"
print bubbleSort(arr)

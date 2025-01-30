def arrFill(arr)
  print "podaj ilość liczb w tabeli: "
  n = gets.chomp.to_i

  while n > 0
    print "podaj liczbe: "
    a = gets.chomp.to_i
    arr << a
    n -= 1
  end

  return arr
end

def quickSort(arr, low = 0, high = nil)
  if high == nil
    high = arr.length - 1
  end

  if low < high
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot, high)
  end

  return arr
end

def partition(arr, low, high)
  pivot = arr[high]
  i = low - 1

  (low..high-1).each do |j|
    if arr[j] <= pivot
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
    end
  end

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1
end

arr = []

arrFill(arr)
print quickSort(arr)

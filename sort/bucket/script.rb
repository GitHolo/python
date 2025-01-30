def arrFill(arr)

  print "podaj ilość liczb w tabeli: "
  n = gets.chomp.to_i

  while n>0
    print "podaj liczbe: "
    a = gets.chomp.to_f
    b = a.to_s.length
    arr << a/10**(b-2)
    n-=1
  end

  return arr

end

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


def bucketSort(arr)
  n = arr.length
  buckets = Array.new(n) { [] }

  arr.each do |num|
    bi = n*num
    buckets[bi] << num
  end

  buckets.each do |bucket|
    insertSort(bucket)
  end

  index = 0

  buckets.each do |bucket|
    bucket.each do |num|
      arr[index] = num
      index += 1
    end
  end

end


arr = []

print arrFill(arr),"\n"
print bucketSort(arr)

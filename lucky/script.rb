def lucky(limit)

  arr = (1..limit).to_a
  n = 1

  while n< arr.length

    step = arr[n]
    arr = arr.each_with_index.reject { |num, i| (i + 1) % step == 0 }.map(&:first)
    n+=1

  end

  return arr

end

print lucky(1500)

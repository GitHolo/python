def median(arr)
  n = arr.length
  arr = arr.sort
  if n%2==0
    n/=2
    return arr[(n+(n+1))/2-1]
  else
    return arr[(n+1)/2]
  end
end

arr = [23, 11, 123213, 1134, 21,3]
print arr,"\n"
puts "median: ",median(arr)

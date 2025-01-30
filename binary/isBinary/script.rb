def isBinary(n)

  n.to_s.each_char do |i|

    if !['0', '1'].include?(i.to_s)

      return false

    end
  end

  return true

end

print isBinary(10111)

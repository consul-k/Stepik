res = 0
hash.each { |x, y| res += y if y%2 != 0 }
puts res

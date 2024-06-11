n = gets.to_i

first_digit = n
while first_digit >= 10 do
  first_digit /= 10
end

puts first_digit

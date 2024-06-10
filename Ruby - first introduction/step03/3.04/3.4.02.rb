x = gets.to_i
if x == 6
    puts "Суббота"
elsif x == 7
    puts "Воскресенье"
elsif x <= 5
    puts "Рабочий день"
else
    puts "Неправильный день"
end

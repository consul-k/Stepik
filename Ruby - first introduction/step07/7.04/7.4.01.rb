# текущее время
t = Time.now
puts t

# год, месяц, день
puts t.year
puts t.month
puts t.day

# произвольная дата
t = Time.new(1986, 4, 26)
puts t

# день недели: 0 это воскресенье
puts t.wday

# день года
puts t.yday

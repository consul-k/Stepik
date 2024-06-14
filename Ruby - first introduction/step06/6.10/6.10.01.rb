class Player
  attr_accessor :name, :health, :power
  def initialize(n, h, pow)
    @name = n
    @health = h
    @power = pow
  end
  def isAlive
    @health > 0
  end
  def hit(opponent)
    opponent.health -= self.power
  end
  def to_s
    "#{name}: Здоровье: #{health}, Сила: #{power}"
  end
end

def fight(p1, p2)
  while p1.isAlive && p2.isAlive
    p1.hit(p2)
    p2.hit(p1)      
    show_info(p1, p2)
  end

  if p1.isAlive 
    puts "#{p1.name} ПОБЕДИЛ!" 
  elsif p2.isAlive
    puts "#{p2.name} ПОБЕДИЛ!" 
  else
    puts "НИЧЬЯ!"
  end
end

def show_info(*p)
  p.each { |x| puts x}
end

# создаем игроков
puts "ИНФОРМАЦИЯ ОБ ИГРОКАХ"
p1 = Player.new("Игрок 1", 1 + rand(100), 1 + rand(20))
p2 = Player.new("Игрок 2", 1 + rand(100), 1 + rand(20))

# показываем информацию об игроках
show_info(p1, p2)

puts "ДА НАЧНЕТСЯ БОЙ!"
fight(p1, p2)

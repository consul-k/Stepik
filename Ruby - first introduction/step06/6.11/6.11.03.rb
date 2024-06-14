n = gets
c = gets
class Automobile
  def initialize(name, color)
    @name = name
    @color = color
  end
  public
  attr_accessor :name
  attr_accessor :color
end

ford = Automobile.new(n, c)
puts ford.name
puts ford.color

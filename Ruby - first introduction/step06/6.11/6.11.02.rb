x = gets.chomp

class Writer
  def initialize(x)
    @text = x
  end
  def back
    @text
  end
end

book = Writer.new(x)
puts book.back

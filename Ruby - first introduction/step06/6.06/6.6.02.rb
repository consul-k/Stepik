class Animal
    def voice
        puts "Муу"
    end
end

class Cow < Animal
end

x = Cow.new
x.voice

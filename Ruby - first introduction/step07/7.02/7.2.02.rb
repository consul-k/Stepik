module Car
    class Volvo
        @@wheels = 4
        def how_many_wheels
            puts @@wheels
        end
    end 
end

module Truck
    class Volvo
        @@wheels = 6
        def how_many_wheels
            puts @@wheels
        end
    end
end

a = Car::Volvo.new
b = Truck::Volvo.new

a.how_many_wheels
b.how_many_wheels

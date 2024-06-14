module Fire
    def firearms
        puts "Огнестрельное оружие!"
    end
end

module Cold
    def cold_steel
        puts "Холодное оружие!"
    end
end

class Weapon
    def define
        puts "Оружие!"
    end
end

class Knife < Weapon
    include Cold
end

class Bow < Weapon
    include Cold
end

class Gun < Weapon
    include Fire
end

class Rifle < Weapon
    include Fire
end

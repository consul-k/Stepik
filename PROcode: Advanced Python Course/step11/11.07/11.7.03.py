total_energy = 100

def energy_control():
    global total_energy
    total_energy -= 20

    room = 0

    def room_energy():
        nonlocal room
        room = 30

    room_energy()
    return total_energy, room

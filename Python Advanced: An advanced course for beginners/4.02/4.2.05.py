def get_strongest_avenger(names, powers):
    max_power = powers[0]
    max_index = 0
    for i in range(1, len(powers)):
        if powers[i] > max_power:
            max_power = powers[i]
            max_index = i
    return names[max_index]

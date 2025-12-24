import math

def fight_boss(attacks, boss_defense):
    best_attack = None
    max_damage = -1
    
    for attack in attacks:
        base_damage = attack["power"]
        
        if attack["type"] == boss_defense["weakness"]:
            base_damage = math.ceil(base_damage * 1.5)
        
        total_defense = boss_defense["armor"] + boss_defense["shield"]
        final_damage = max(0, base_damage - total_defense)
        
        if final_damage > max_damage:
            max_damage = final_damage
            best_attack = attack["name"]
    
    result_message = "Победа!" if max_damage > 100 else "Босс выжил..."
    
    return best_attack, max_damage, result_message

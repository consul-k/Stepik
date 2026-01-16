def find_ghost_location(real_moves, fake_routes):
    for date, real_city in real_moves.items():
        if date not in fake_routes:
            return f"🔥 Призрак пойман в городе: {real_city}!"
        
        if fake_routes[date] != real_city:
            return f"🔥 Призрак пойман в городе: {real_city}!"
    
    for date in fake_routes:
        if date not in real_moves:
            return f"🔥 Призрак пойман в городе: {fake_routes[date]}!"
    
    return "👻 Призрак снова скрылся..."

import ast
import sys

line1 = input().strip()
line2 = input().strip()

real_moves = ast.literal_eval(line1)
fake_routes = ast.literal_eval(line2)

result = find_ghost_location(real_moves, fake_routes)
print(result)

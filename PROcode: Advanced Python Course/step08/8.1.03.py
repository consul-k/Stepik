def find_ghost_network(data, target_id):
    if target_id not in data:
        print("ID не найден.")
        return
    
    accounts = data[target_id]
    
    print(f"Призрак найден на {len(accounts)} платформ(ах):")
    for nickname, platform in accounts:
        print(f"- {platform}: {nickname}")

import ast
data_str = input().strip()
target_id = input().strip()

data = ast.literal_eval(data_str)

find_ghost_network(data, target_id)

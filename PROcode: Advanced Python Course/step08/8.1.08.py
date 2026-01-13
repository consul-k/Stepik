data_input = input()
data = eval(data_input)

seen_ips = {}
found_ghost = False

for nickname, raw_ip in data.items():
    if not raw_ip:
        continue
    
    ip = raw_ip.strip()
    
    if not ip:
        continue

    if ip in seen_ips:
        first_user = seen_ips[ip]
        print(f"Настоящий хакер: {first_user}, {nickname} (IP: {ip})")
        found_ghost = True
        break
    else:
        seen_ips[ip] = nickname

if not found_ghost:
    print("Призрак не найден")

def find_true_ip(ip_dict):
    for ip, status in ip_dict.items():
        if status:
            return ip
    return None
  
input_data = input()

input_data = input_data.replace('false', 'False').replace('true', 'True')
ip_dict = eval(input_data)

true_ip = find_true_ip(ip_dict)

print(f"Истинный адрес: {true_ip}")

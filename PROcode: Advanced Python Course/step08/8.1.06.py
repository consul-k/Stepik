import sys

try:
    data = eval(input()) 
except:
    data = {"192.168.1.1": {"google.com": 5, "darkweb.net": 12, "forum.xyz": 7}, "10.0.0.23": {"google.com": 2, "darkweb.net": 1, "forum.xyz": 5}}

most_active_ip = None
max_total_activity = -1

for ip, sites in data.items():
    current_activity = sum(sites.values())
    
    if current_activity > max_total_activity:
        max_total_activity = current_activity
        most_active_ip = ip

most_visited_site = None
max_site_visits = -1

if most_active_ip:
    sites_of_hacker = data[most_active_ip]
    
    for site, count in sites_of_hacker.items():
        if count > max_site_visits:
            max_site_visits = count
            most_visited_site = site

print(f"Самый активный IP: {most_active_ip}")
print(f"Наиболее посещаемый сайт: {most_visited_site}")

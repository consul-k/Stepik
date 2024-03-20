current_hours = int(input())
current_mins = int(input())

total_secs = current_hours * 3600 + current_mins * 60
secs_to_midnight = 86400 - total_secs

print(secs_to_midnight)

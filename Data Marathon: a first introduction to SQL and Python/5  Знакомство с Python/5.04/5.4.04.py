import pandas as pd

count_events = game_events[game_events['user_id'] == 'f5ef9841']['event_name'].count()
print(count_events)

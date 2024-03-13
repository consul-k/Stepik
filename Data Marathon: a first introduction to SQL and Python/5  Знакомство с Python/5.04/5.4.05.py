import pandas as pd

count_events = game_events[game_events['event_date'] == '2021-01-15']['event_name'].count()
print(count_events)

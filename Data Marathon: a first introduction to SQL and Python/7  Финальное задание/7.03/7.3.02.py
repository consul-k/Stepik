import pandas as pd

game_events_filtered = game_events[game_events['revenue'] > 0]
arppu = game_events['revenue'].sum() / game_events_filtered['user_id'].nunique()
print(arppu)

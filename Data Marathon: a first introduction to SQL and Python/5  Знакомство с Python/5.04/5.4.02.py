import pandas as pd

max_date = game_events['event_date'].max()
min_date = game_events['event_date'].min()

print(max_date, min_date)

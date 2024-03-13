import pandas as pd

game_events_unique_users = game_events['user_id'].nunique()
print(game_events_unique_users)

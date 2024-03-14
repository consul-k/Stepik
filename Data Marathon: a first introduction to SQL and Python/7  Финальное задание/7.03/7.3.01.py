import pandas as pd

arpu = game_events['revenue'].sum()/ game_events['user_id'].nunique()
print(arpu)

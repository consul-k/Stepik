import pandas as pd

mean_revenue = game_events['revenue'].mean()
median_revenue = game_events['revenue'].median()

print(mean_revenue, median_revenue)

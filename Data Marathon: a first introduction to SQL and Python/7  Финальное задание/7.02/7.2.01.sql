SELECT SUM(revenue) / COUNT(DISTINCT user_id) as arpu
FROM game_events

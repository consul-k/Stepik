SELECT SUM(revenue) / COUNT(DISTINCT user_id) as arppu
FROM game_events
WHERE revenue > 0

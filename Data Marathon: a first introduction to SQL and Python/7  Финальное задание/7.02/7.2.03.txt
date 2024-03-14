SELECT sum(revenue)/count(event_name) as aov
FROM game_events
WHERE event_name = 'in_app_purchase'

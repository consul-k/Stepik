friends_anna = {'Иван', 'Мария', 'Петр', 'Елена'}
friends_boris = {'Петр', 'Елена', 'Сергей', 'Анна'}

common_friends = sorted(friends_anna & friends_boris)
print(common_friends)

all_friends = sorted(friends_anna | friends_boris)
print(all_friends)

unique_anna_friends = sorted(friends_anna - friends_boris)
print(unique_anna_friends)

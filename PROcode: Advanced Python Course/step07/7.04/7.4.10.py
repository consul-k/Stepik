n = int(input())

users = {}

for _ in range(n):
    name, likes_str, comments_str = input().split()
    likes = int(likes_str)
    comments = int(comments_str)
    
    key = name.lower()
    
    if key in users:
        first_name, total_likes, total_comments = users[key]
        users[key] = (first_name, total_likes + likes, total_comments + comments)
    else:
        users[key] = (name, likes, comments)

for key in users:
    name, total_likes, total_comments = users[key]
    print(f"{name} {total_likes} {total_comments}")

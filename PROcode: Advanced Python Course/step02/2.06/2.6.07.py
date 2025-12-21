p = int(input())

movies = []
for _ in range(p):
    movie = input()
    movies.append(movie)

new_title = input()

movies_copy = movies.copy()

print(movies)
print(movies_copy)

movies_copy.append(new_title)

print(movies)
print(movies_copy)

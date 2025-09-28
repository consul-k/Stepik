input_str = input()

anime_list = [anime.strip() for anime in input_str.split(',')]

anime_frozen_set = frozenset(anime_list)

print(sorted(anime_frozen_set))

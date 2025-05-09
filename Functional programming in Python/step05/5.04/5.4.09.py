from collections import defaultdict

def print_order_rating(data):
    ratings = defaultdict(list)
    for name, score in data:
        ratings[name].append(score)

    average_ratings = []
    for name, scores in ratings.items():
        avg = sum(scores) / len(scores)
        average_ratings.append((name, avg))

    average_ratings.sort(key=lambda x: (-x[1], x[0].lower()))

    for name, avg in average_ratings:
        print(name, round(avg, 3))

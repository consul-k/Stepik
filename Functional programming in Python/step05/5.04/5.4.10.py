def print_statistic(data):
    from collections import defaultdict

    authors = defaultdict(set)

    for author, commenter in data:
        if author != commenter:  # не учитываем самокомментарии
            authors[author].add(commenter)

    # Преобразуем в список кортежей: (автор, количество уникальных комментаторов)
    stats = [(author, len(commenters)) for author, commenters in authors.items()]

    # Сортировка: сначала по убыванию количества комментаторов, затем по алфавиту (без учёта регистра)
    stats.sort(key=lambda x: (-x[1], x[0].lower()))

    # Печать результата
    for author, count in stats:
        print(f"Количество уникальных комментаторов у {author} - {count}")

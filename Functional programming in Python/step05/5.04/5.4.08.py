def print_best_and_worst_laureate(awards):

    laureate_counts = {}
    for winner in awards.values():
        if winner not in laureate_counts:
            laureate_counts[winner] = 0
        laureate_counts[winner] += 1

    max_awards = max(laureate_counts.values())
    min_awards = min(laureate_counts.values())

    best_laureates = [laureate for laureate, count in laureate_counts.items() if count == max_awards]
    worst_laureates = [laureate for laureate, count in laureate_counts.items() if count == min_awards]

    print(f"{', '.join(best_laureates)}, {max_awards}")
    print(f"{', '.join(worst_laureates)}, {min_awards}")

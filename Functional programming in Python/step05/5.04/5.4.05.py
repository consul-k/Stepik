def get_sort_lines(lines):
    return sorted(
        lines,
        key=lambda line: (abs(line[1] - line[0]), line[0], line[1])
    )

N = int(input())

tasks = {}

for _ in range(N):
    task, theme = input().split(' - ')
    if theme not in tasks:
        tasks[theme] = []
    tasks[theme].append(task)

interested_themes = input().split(',')

result_tasks = []
for theme in interested_themes:
    theme = theme.strip()
    if theme in tasks:
        result_tasks.extend(tasks[theme])

print(' '.join(sorted(result_tasks)))

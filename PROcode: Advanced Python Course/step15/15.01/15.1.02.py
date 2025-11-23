input_string = input().strip()

themes_list = input_string.split(',')

themes_list = [theme.strip() for theme in themes_list]

themes_list.sort()

for theme in themes_list:
    print(theme)

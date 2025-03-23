def red():
    return 'Color is red'

def green():
    return 'Color is green'

def blue():
    return f'Color is blue'

colors = {}
colors[green] = '00FF00'
colors[blue] = '0000FF'
colors[red] = 'FF0000'

for i in colors:
    print(f'{i()} - {colors[i]}')

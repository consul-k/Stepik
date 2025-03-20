def info_kwargs(**kwargs):
    for i in sorted(kwargs.keys()):
        print(f'{i} = {kwargs[i]}')

while True:
    try:
        nickname = input()
        if '_' not in nickname:
            print(nickname)
            break
    except EOFError:
        break

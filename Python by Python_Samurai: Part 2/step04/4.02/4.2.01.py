numbers = list(map(int, input().split()))
match numbers:
    case [first, *_, last]:
        print(first, last)

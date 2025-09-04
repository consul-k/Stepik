nya = int(input())

meow = input().split()

print(any([nya - int(kitty) >= 0 for kitty in meow]))

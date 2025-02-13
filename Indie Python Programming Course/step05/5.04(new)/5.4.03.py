elements = input().split()

elements = [int(element) for element in elements]

r = int(input())

found = False
for index, element in enumerate(elements):
    if element == r:
        print(index + 1)
        found = True
        break
        
if not found:
    print("ErrorValue")

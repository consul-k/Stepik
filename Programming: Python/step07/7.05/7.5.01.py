def find_position(heights, petya_height):
    position = 0
    while position < len(heights) and heights[position] >= petya_height:
        position += 1
    return position + 1

n = int(input())
heights = list(map(int, input().split()))
petya_height = int(input())

position = find_position(heights, petya_height)

print(position)

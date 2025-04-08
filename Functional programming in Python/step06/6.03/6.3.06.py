def from_hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)
    
    return (red, green, blue)

def convert_to_rgb(hex_colors):
    return [from_hex_to_rgb(color) for color in hex_colors]

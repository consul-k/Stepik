def next_state(height, width, grid):
    # Создаем новое поле с теми же размерами
    new_grid = [['.' for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            # Считаем количество живых соседей
            live_neighbors = 0
            
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue  # Пропускаем саму клетку
                    
                    ni = (i + di) % height  # Используем торoidal обертку
                    nj = (j + dj) % width   # Используем торoidal обертку

                    if grid[ni][nj] == 'X':
                        live_neighbors += 1
            
            # Применяем правила "Игры жизни"
            if grid[i][j] == 'X':
                if live_neighbors in (2, 3):
                    new_grid[i][j] = 'X'
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = 'X'
    
    return new_grid

def main():
    import sys
    
    # Чтение высоты и ширины поля
    input_lines = sys.stdin.read().strip().splitlines()
    height, width = map(int, input_lines[0].split())
    
    # Чтение состояния поля
    grid = [list(line) for line in input_lines[1:]]
    
    # Получение следующего состояния поля
    new_grid = next_state(height, width, grid)
    
    # Вывод нового состояния поля
    for row in new_grid:
        print(''.join(row))

if __name__ == "__main__":
    main()

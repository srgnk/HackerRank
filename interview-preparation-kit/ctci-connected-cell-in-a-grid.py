def find_adjacent(grid, i, j):
    count = 0
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0
    if grid[i][j] == 0:
        return 0
    
    count += 1
    grid[i][j] -= 1
    
    count += find_adjacent(grid, i-1, j-1)
    count += find_adjacent(grid, i-1, j)
    count += find_adjacent(grid, i-1, j+1)
    count += find_adjacent(grid, i+1, j-1)
    count += find_adjacent(grid, i+1, j)
    count += find_adjacent(grid, i+1, j+1)
    count += find_adjacent(grid, i, j-1)
    count += find_adjacent(grid, i, j+1)
    
    return count

def get_biggest_region(grid):
    biggest = 0
    for i in range(n):
        for j in range(m):
            result = find_adjacent(grid, i, j)
            if result > biggest:
                biggest = result
    return biggest

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)

print(get_biggest_region(grid))

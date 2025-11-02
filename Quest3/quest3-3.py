def digable(grid, row, col):
     val = grid[row][col]
     if val == 0 or row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1:
          return False

     for delta_row in [-1, 0, 1]:
           for delta_col in [-1, 0, 1]:
                 if grid[row + delta_row][col + delta_col] < val:
                       return False     

     return True


with open("quest3-3.txt", "r") as file:
     data = file.read()
     grid = [list(row) for row in data.split("\n")]


for i in range(len(grid)):
     for j in range(len(grid[0])):
          if grid[i][j] == '#':
               grid[i][j] = 1
          else:
               grid[i][j] = 0

updated = 1
while updated > 0:
     updated = 0
     for i in range(len(grid)):
          for j in range(len(grid[0])):
               if digable(grid, i, j):
                    grid[i][j] += 1
                    updated += 1

total = sum([sum(row) for row in grid])
print(total)

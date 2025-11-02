def digable(grid, row, col):
     val = grid[row][col]
     if val == 0:
          return False
     if row > 0:
          if grid[row - 1][col] < val:
               return False
     if row < len(grid) - 1:
          if grid[row + 1][col] < val:
               return False
     if col > 0:
          if grid[row][col - 1] < val:
               return False
     if col < len(grid[0]) - 1:
          if grid[row][col + 1] < val:
               return False

     return True


with open("quest3-1.txt", "r") as file:
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

grids = []

with open("quest10-2.txt", "r") as file:
     grid_blocks = file.read().split("\n\n")
     for block in grid_blocks:
          block_rows = block.split('\n')
          new_grids = [[] for _ in range(len(block_rows[0].split(" ")))]
          for row in block_rows:
               for idx, segment in enumerate(row.split(" ")):
                    new_grids[idx].append(segment)

          grids += new_grids

power = 0
for grid in grids:
     rows = []
     cols = []
     for i in range(4):
          new_row = [grid[i + 2][0], grid[i + 2][1], grid[i + 2][-2], grid[i + 2][-1]]
          rows.append(new_row)
          new_col = [grid[0][i + 2], grid[1][i + 2], grid[-2][i + 2], grid[-1][i + 2]]
          cols.append(new_col)

     for i in range(4):
          for j in range(4):
               for letter in rows[i]:
                    if letter in cols[j]:
                         power += (i * 4 + j + 1) * (ord(letter) - 64)
                         break


print(power)

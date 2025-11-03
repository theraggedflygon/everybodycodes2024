grids = []

with open("quest10-3.txt", "r") as file:
     grid_data = file.read().split("\n")
     big_grid = [list(row) for row in grid_data]

row = 0
col = 0
DIM = 8
power = 0
while row + 8 <= len(big_grid):
     while col + 8 <= len(big_grid[row]):
          small_grid = []
          for i in range(DIM):
               small_grid.append(big_grid[row + i][col: col + DIM])
          small_rows = []
          small_cols = []
          rune_word = ["_" for _ in range((DIM // 2) ** 2)]
          for i in range(DIM // 2):
               new_row = [small_grid[i + 2][0], small_grid[i + 2][1], small_grid[i + 2][-2], small_grid[i + 2][-1]]
               if new_row.count("?") > 1:
                    print(new_row)
               small_rows.append(new_row)
               new_col = [small_grid[0][i + 2], small_grid[1][i + 2], small_grid[-2][i + 2], small_grid[-1][i + 2]]
               small_cols.append(new_col)
          needs_fill = []
          for i in range(DIM // 2):
               for j in range(DIM // 2):
                    for letter in small_rows[i]:
                         if letter == '?':
                              continue
                         elif letter in small_cols[j]:
                              rune_word[i * 4 + j] = letter
                              break
                    if rune_word[i * 4 + j] == "_":
                         needs_fill.append((i, j))
          for i, j in needs_fill:
               if '?' in small_rows[i]:
                    question_idx = small_rows[i].index('?')
                    for letter in small_cols[j]:
                         if letter not in rune_word:
                              rune_word[i * 4 + j] = letter
                              if question_idx < 2:
                                   big_grid[row + 2 + i][col + question_idx] = letter
                              else:
                                   big_grid[row + 2 + i][col + question_idx + 4] = letter
               elif '?' in small_cols[j]:
                    question_idx = small_cols[j].index('?')
                    for letter in small_rows[i]:
                         if letter not in rune_word:
                              rune_word[i * 4 + j] = letter
                              if question_idx < 2:
                                   big_grid[row + question_idx][col + 2 + i] = letter
                              else:
                                   big_grid[row + question_idx + 4][col + 2 + i] = letter
               else:
                    break
          if '_' not in rune_word:
               for idx, letter in enumerate(rune_word):
                    power += (idx + 1) * (ord(letter) - 64)
          print(rune_word, power)
          col += DIM - 2
     col = 0
     row += DIM - 2

print(power)

# power = 0
# for grid in grids:
#      rows = []
#      cols = []
#      for i in range(4):
#           new_row = [grid[i + 2][0], grid[i + 2][1], grid[i + 2][-2], grid[i + 2][-1]]
#           rows.append(new_row)
#           new_col = [grid[0][i + 2], grid[1][i + 2], grid[-2][i + 2], grid[-1][i + 2]]
#           cols.append(new_col)

#      for i in range(4):
#           for j in range(4):
#                for letter in rows[i]:
#                     if letter in cols[j]:
#                          power += (i * 4 + j + 1) * (ord(letter) - 64)
#                          break


# print(power)

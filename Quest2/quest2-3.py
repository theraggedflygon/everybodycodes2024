def get_word(grid, row, col, row_dir, col_dir, length):
     word = ""
     coords = []
     for i in range(length):
          if row + row_dir * i < 0 or row + row_dir * i >= len(grid):
               return word, coords
          word += grid[row + row_dir * i][(col + col_dir * i) % len(grid[0])]
          coords.append((row + row_dir * i, (col + col_dir * i) % len(grid[0])))
     return word, coords



with open("quest2-3.txt", "r") as file:
     rune_text, scale_text = file.read().split("\n\n")
     grid = scale_text.split("\n")

runes = rune_text[rune_text.index(":") + 1:].split(",")
check_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
max_rune_len = max([len(rune) for rune in runes])


for i in range(len(grid)):
     for j in range(len(grid[0])):
          for row_delta, col_delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
               word, coords = get_word(grid, i, j, row_delta, col_delta, max_rune_len)
               for rune in runes:
                    if word.startswith(rune):
                         for k in range(len(rune)):
                              mark_row, mark_col = coords[k]
                              check_grid[mark_row][mark_col] = 1

total = sum(sum(row) for row in check_grid)
print(total)

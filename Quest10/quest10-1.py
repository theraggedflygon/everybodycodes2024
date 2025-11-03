with open("quest10-1.txt", "r") as file:
     grid = file.read().split("\n")

rows = []
cols = []
for i in range(4):
     new_row = [grid[i + 2][0], grid[i + 2][1], grid[i + 2][-2], grid[i + 2][-1]]
     rows.append(new_row)
     new_col = [grid[0][i + 2], grid[1][i + 2], grid[-2][i + 2], grid[-1][i + 2]]
     cols.append(new_col)

answer = ""
for i in range(4):
     for j in range(4):
          for letter in rows[i]:
               if letter in cols[j]:
                    answer += letter

print(answer)

VISITED_BASES = []
def generate_perms(options, base):
     if base in VISITED_BASES:
          return []
     VISITED_BASES.append(base)
     if len(options) == 1:
          return [[options[0]]]
     all_perms = []
     for idx, elem in enumerate(options):
          others = options[:idx] + options[idx + 1:]
          sub_perms = generate_perms(others, base + elem)
          if sub_perms == []:
               continue
          for perm in sub_perms:
               all_perms.append([elem] + perm)
     return all_perms

def generate_score(track, path, laps):
     score = 0
     current_power = 10
     lap = 0
     pos = 0
     while lap < laps:
          if track[pos % len(track)] == '+':
               current_power += 1
          elif track[pos % len(track)] == '-' and current_power > 0:
               current_power -= 1
          else:
               if track[pos % len(track)] == 'S':
                    lap += 1
               if path[pos % len(path)] == '+':
                    current_power += 1
               elif path[pos % len(path)] == '-' and current_power > 0:
                    current_power -= 1
          score += current_power
          pos += 1
     return score


with open("quest7-3.txt", "r") as file:
     data = file.read()

with open("quest7-3_track.txt", 'r') as file:
     track_data = file.read().split("\n")
     track_grid = [list(row) for row in track_data]
     max_row_chars = 0
     for row in track_grid:
          if len(row) > max_row_chars:
               max_row_chars = len(row)

     for row in track_grid:
          while len(row) < max_row_chars:
               row.append(" ")

     row = 0
     col = 2
     visited = [(0, 1), (0, 2)]
     track_str = track_grid[0][1] + track_grid[0][2]
     while True:
          if row < len(track_grid) - 1 and (row + 1, col) not in visited and track_grid[row + 1][col] != " ":
               row += 1
          elif row > 0 and (row - 1, col) not in visited and track_grid[row - 1][col] != " ":
               row -= 1
          elif col < len(track_grid[0]) - 1 and (row, col + 1) not in visited and track_grid[row][col + 1] != " ":
               col += 1
          elif col > 0 and (row, col - 1) not in visited and track_grid[row][col - 1] != " ":
               col -= 1   
          
          visited.append((row, col))
          track_str += track_grid[row][col]
          if track_grid[row][col] == 'S':
               break

options = list('+' * 5 + '-' * 3 + '=' * 3)
all_paths = generate_perms(options, "")
     
LAPS = 2024

_, opp_path = data.split(":")
opp_path = opp_path.split(",")
opp_score = generate_score(track_str, opp_path, LAPS)

wins = 0
for idx, path in enumerate(all_paths):
     if generate_score(track_str, path, LAPS) > opp_score:
          wins += 1

print(wins)
     
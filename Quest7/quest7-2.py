with open("quest7-2.txt", "r") as file:
     data = file.read().split('\n')

with open("quest7-2_track.txt", 'r') as file:
     track_data = file.read().split("\n")
     track_str = ""
     track_str += track_data[0][1:]
     left_seg = ""
     for row in track_data[1:-1]:
          track_str += row[-1]
          left_seg += row[0]
     track_str += track_data[-1][::-1]
     track_str += left_seg[::-1]
     track_str += 'S'
     
LAPS = 10

scores = {}
for row in data:
     name, path = row.split(":")
     path = path.split(",")
     name_score = 0
     current_power = 10
     lap = 0
     pos = 0
     while lap < LAPS:
          if track_str[pos % len(track_str)] == '+':
               current_power += 1
          elif track_str[pos % len(track_str)] == '-' and current_power > 0:
               current_power -= 1
          else:
               if track_str[pos % len(track_str)] == 'S':
                    lap += 1
               if path[pos % len(path)] == '+':
                    current_power += 1
               elif path[pos % len(path)] == '-' and current_power > 0:
                    current_power -= 1
          name_score += current_power
          pos += 1
     scores[name] = name_score

print(scores)
sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
print("".join(sorted_scores.keys()))
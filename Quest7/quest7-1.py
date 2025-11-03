with open("quest7-1.txt", "r") as file:
     data = file.read().split('\n')

SEGMENTS = 10

scores = {}
for row in data:
     name, path = row.split(":")
     path = path.split(",")
     name_score = 0
     current_power = 10
     for i in range(SEGMENTS):
          if path[i % len(path)] == '+':
               current_power += 1
          elif path[i % len(path)] == '-' and current_power > 0:
               current_power -= 1
          name_score += current_power
     scores[name] = name_score

sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
print("".join(sorted_scores.keys()))
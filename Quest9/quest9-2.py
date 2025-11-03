with open("quest9-2.txt", "r") as file:
     data = file.read().split("\n")
     targets = [int(num) for num in data]

max_target = max(targets)
min_beetles = [None for _ in range(max_target + 1)]
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
min_beetles[0] = 0

for i in range(max_target):
     for stamp in stamps:
          if i + stamp > max_target:
               break
          if min_beetles[i + stamp] is None or min_beetles[i + stamp] > min_beetles[i] + 1:
               min_beetles[i + stamp] = min_beetles[i] + 1

total = 0
for target in targets:
     total += min_beetles[target]

print(total)

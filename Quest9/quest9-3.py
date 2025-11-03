with open("quest9-3.txt", "r") as file:
     data = file.read().split("\n")
     targets = [int(num) for num in data]

max_target = max(targets) // 2 + 50
min_beetles = [None for _ in range(max_target + 1)]
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
min_beetles[0] = 0

for i in range(max_target):
     for stamp in stamps:
          if i + stamp > max_target:
               break
          if min_beetles[i + stamp] is None or min_beetles[i + stamp] > min_beetles[i] + 1:
               min_beetles[i + stamp] = min_beetles[i] + 1

total = 0
for target in targets:
     mid_target = target // 2
     odd = 0
     if target % 2 == 0:
          min_sum = min_beetles[mid_target] * 2
     else:
          min_sum = min_beetles[mid_target + 1] + min_beetles[mid_target]
          odd = 1
     for offset in range(1, 51):
          if odd and offset == 50:
               continue
          new_sum = min_beetles[mid_target + odd + offset] + min_beetles[mid_target - offset]
          if new_sum < min_sum:
               min_sum = new_sum
     total += min_sum

print(total)
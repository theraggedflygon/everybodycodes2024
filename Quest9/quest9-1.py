with open("quest9-1.txt", "r") as file:
     data = file.read().split("\n")

stamps = [10, 5, 3, 1]

beetles = 0
for row in data:
     target = int(row)
     stamp_idx = 0
     while target > 0:
          if target >= stamps[stamp_idx]:
               beetles += target // stamps[stamp_idx]
               target %= stamps[stamp_idx]
          else:
               stamp_idx += 1

print(beetles)
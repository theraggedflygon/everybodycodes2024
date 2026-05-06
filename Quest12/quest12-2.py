with open("quest12-2.txt", "r") as file:
    data = file.read().split("\n")[::-1]

targets = []
for y, row in enumerate(data[1:]):
    for x, col in enumerate(row[1:]):
        if col == "T" or col == "H":
            targets.append((x, y, col))

total = 0
for x, y, col in targets:
    segment = (y + x) % 3
    power = ((y + x) - segment) // 3
    if col == "T":
        total += (segment + 1) * power
    if col == "H":
        total += (segment + 1) * power * 2

print(total)

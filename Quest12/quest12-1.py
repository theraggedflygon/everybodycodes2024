with open("quest12-1.txt", "r") as file:
    data = file.read().split("\n")[::-1]

targets = []
for y, row in enumerate(data[1:]):
    for x, col in enumerate(row[1:]):
        if col == "T":
            targets.append((x, y))

total = 0
for x, y in targets:
    segment = (y + x) % 3
    power = ((y + x) - segment) // 3
    total += (segment + 1) * power

print(total)

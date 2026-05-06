spawns = dict()
DAYS = 4

with open("quest11-1.txt", "r") as file:
    data = file.read().split("\n")
    for row in data:
        parent, offspring = row.split(":")
        offspring = offspring.split(",")
        spawns[parent] = offspring

old_counts = {key: 0 for key in spawns}
old_counts["A"] = 1

for _ in range(DAYS):
    new_counts = {key: 0 for key in spawns}
    for key, count in old_counts.items():
        offspring = spawns[key]
        for child in offspring:
            new_counts[child] += count

    old_counts = new_counts

total = 0
for count in new_counts.values():
    total += count

print(total)

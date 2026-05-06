spawns = dict()
DAYS = 20

with open("quest11-3.txt", "r") as file:
    data = file.read().split("\n")
    for row in data:
        parent, offspring = row.split(":")
        offspring = offspring.split(",")
        spawns[parent] = offspring

global_min = 10000000000000000000000
global_max = 0

for starter in spawns:
    old_counts = {key: 0 for key in spawns}
    old_counts[starter] = 1

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

    if total < global_min:
        global_min = total
    elif total > global_max:
        global_max = total

print(global_max - global_min)

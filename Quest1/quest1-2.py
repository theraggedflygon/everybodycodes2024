with open("quest1-2.txt", 'r') as file:
    data = file.read()

points = {'A': 0, 'B': 1, 'C': 3, 'D': 5}

score = 0
for i in range(len(data) // 2):
    if data[i * 2] == "x":
        if data[i * 2 + 1] == 'x':
            continue
        score += points[data[i * 2 + 1]]
    elif data[i * 2 + 1] == 'x':
        score += points[data[i * 2]]
    else:
        score += points[data[i * 2]] + 1
        score += points[data[i * 2 + 1]] + 1


print(score)
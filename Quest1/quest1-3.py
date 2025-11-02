with open("quest1-3.txt", 'r') as file:
    data = file.read()

points = {'A': 0, 'B': 1, 'C': 3, 'D': 5}

score = 0
for i in range(len(data) // 3):
    x_count = 0
    for j in range(3):
        if data[i * 3 + j] == 'x':
            x_count += 1
        else:
            score += points[data[i * 3 + j]]
    if x_count == 1:
        score += 2
    elif x_count == 0:
        score += 6


print(score)
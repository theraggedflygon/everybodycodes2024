with open("quest1-1.txt", 'r') as file:
    data = file.read()

score = 0
for i in range(len(data)):
    if data[i] == 'B':
        score += 1
    elif data[i] == 'C':
        score += 3

print(score)
import math

with open("quest8-1.txt", "r") as file:
     blocks = int(file.read())

layers = math.ceil(math.sqrt(blocks))
width = 2 * layers - 1
need = layers ** 2 - blocks

print(width, need, width * need)

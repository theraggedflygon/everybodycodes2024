ACOLYTES = 1111
BLOCKS = 20240000

with open("quest8-2.txt", "r") as file:
     priests = int(file.read())

blocks = BLOCKS - 1
layers = 1
thickness = 1
while blocks > 0:
     layers += 1
     thickness *= priests
     thickness %= ACOLYTES
     width = 2 * layers - 1
     blocks -= width * thickness


width = layers * 2 - 1
need = -1 * blocks
print(width * need)

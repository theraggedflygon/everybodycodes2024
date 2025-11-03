ACOLYTES = 10
BLOCKS = 202400000

with open("quest8-3.txt", "r") as file:
     priests = int(file.read())

heights = [1]
layers = 1
thickness = 1

while True:
     print(layers)
     layers += 1
     thickness *= priests
     thickness %= ACOLYTES
     thickness += ACOLYTES
     for i in range(len(heights)):
          heights[i] += thickness
     heights.append(thickness)
     heights.append(thickness)
     blocks_used = sum(heights)
     for i in range(len(heights) - 2):
          removed = (priests * len(heights) * heights[i]) % ACOLYTES
          blocks_used -= removed
     if blocks_used > BLOCKS:
          break

print(layers, blocks_used - BLOCKS)

with open("quest4-2.txt", "r") as file:
     data = file.read()
     nails = [int(num) for num in data.split("\n")]

short = min(nails)

total = 0
for nail in nails:
     total += nail - short

print(total)

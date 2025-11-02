import os

DAY = 2

if os.path.exists(f"Quest{DAY}"):
    exit()

os.mkdir(f"Quest{DAY}")
for i in range(3):
    with open(f"Quest{DAY}/quest{DAY}-{i + 1}.py", 'w') as file:
        file.write(f'with open("quest{DAY}-{i}.txt", "r") as file:\n \
    data = file.read()')
    with open(f"Quest{DAY}/quest{DAY}-{i + 1}.txt", 'w') as file:
        pass

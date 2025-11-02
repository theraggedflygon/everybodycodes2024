with open("quest2-2.txt", "r") as file:
     runes, text = file.read().split("\n\n")

runes = runes[runes.index(":") + 1:].split(",")

count = 0
for line in text.split("\n"):
     rune_check = [0 for _ in range(len(line))]
     for direction, line_dir in enumerate([line, line[::-1]]):
          for i in range(len(line_dir)):
               substr = line_dir[i:]
               for rune in runes:
                    if substr.startswith(rune):
                         if direction == 0:
                              for j in range(len(rune)):
                                   rune_check[i + j] = True
                         else:
                              for j in range(len(rune)):
                                   rune_check[-(i + 1 + j)] = True
     count += sum(rune_check)

print(count)
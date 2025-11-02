with open("quest2-1.txt", "r") as file:
     runes, text = file.read().split("\n\n")

runes = runes[runes.index(":") + 1:].split(",")

count = 0
for i in range(len(text)):
     substr = text[i:]
     for rune in runes:
          if substr.startswith(rune):
               count += 1

print(count)
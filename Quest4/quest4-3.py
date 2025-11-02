with open("quest4-3.txt", "r") as file:
     data = file.read()
     nails = [int(num) for num in data.split("\n")]

short = 0
mid = 0
long = max(nails)

while long >= short:
     if mid == (long + short) // 2:
          break
     mid = (long + short) // 2
     short_total = 0
     long_total = 0
     mid_total = 0
     for nail in nails:
          short_total += abs(nail - short)
          mid_total += abs(nail - mid)
          long_total += abs(nail - long)
     if long_total - mid_total > short_total - mid_total:
          long = mid
     else:
          short = mid

print(mid_total)

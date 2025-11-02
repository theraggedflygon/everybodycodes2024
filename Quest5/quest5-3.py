class Node:
     def __init__(self, value, head):
          self.head = head
          self.tail = None
          self.val = value
     
     def get_end_tail(self):
          if self.tail is None:
               return self
          else:
               return self.tail.get_end_tail()

     def list_out(self):
          if self.tail is None:
               print(self.val)
          else:
               print(str(self.val) + "->", end="")
               self.tail.list_out()


with open("quest5-3.txt", "r") as file:
     rows = file.read().split("\n")

cols = [Node(int(val), None) for val in rows[0].split(" ")]
for row in rows[1:]:
     for idx, val in enumerate(row.split(" ")):
          col_tail = cols[idx].get_end_tail()
          col_tail.tail = Node(int(val), col_tail)

counts = {}
round = 0
while True:
     clapper_col = round % len(cols)
     clapper = cols[clapper_col]
     cols[clapper_col] = clapper.tail
     cols[clapper_col].head = None

     new_col = (clapper_col + 1) % len(cols)
     claps = 1
     side = 'l'
     current = cols[new_col]
     while claps < clapper.val:
          claps += 1
          if side == 'l':
               if current.tail is None:
                    side = 'r'
               else:
                    current = current.tail
          elif side == 'r':
               if current.head is None:
                    side = 'l'
               else:
                    current = current.head
     if side == 'l':
          clapper.head = current.head
          if current.head is not None:
               current.head.tail = clapper
          clapper.tail = current
          current.head = clapper
          if clapper.head is None:
               cols[new_col] = clapper
     else:
          clapper.head = current
          clapper.tail = current.tail
          if current.tail is not None:
               current.tail.head = clapper
          current.tail = clapper
     row_heads = [col.val for col in cols]
     round += 1
     head_str = "".join([str(head) for head in row_heads])
     if head_str in counts:
          counts[head_str] += 1
          if counts[head_str] == 2024:
               break
     else:
          print(round, head_str)
          counts[head_str] = 1

print(max(int(head_str) for head_str in counts))
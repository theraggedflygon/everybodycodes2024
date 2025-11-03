class Node:
     def __init__(self, name, parent, children):
          self.name = name
          self.parent = parent
          self.children = []
          if self.parent is None:
               self.depth = 1
          else:
               self.depth = self.parent.depth + 1
          if name == '@':
               return

          for child in children:
               if child == '@':
                    new_fruit = Node(child, self, None)
                    self.children.append(new_fruit)
                    fruits.append(new_fruit)
               else:
                    if child in row_strs:
                         new_child = Node(child, self, row_strs[child])
                         self.children.append(new_child)
                         nodes_dict[child] = new_child
          

with open("quest6-2.txt", "r") as file:
     rows = file.read().split("\n")

row_strs = dict()
for row in rows:
     name, children = row.split(":")
     row_strs[name] = children.split(",")

nodes_dict = {}
fruits = []

nodes_dict['RR'] = Node('RR', None, row_strs['RR'])

depths = [fruit.depth for fruit in fruits]
counts = {str(depth): depths.count(depth) for depth in depths}
target_depth = None
for depth in counts:
     if counts[depth] == 1:
          target_depth = int(depth)
          break

for fruit in fruits:
     if fruit.depth == target_depth:
          current = fruit
          path = current.name
          while current.parent is not None:
               current = current.parent
               path = current.name[0] + path

print(path)
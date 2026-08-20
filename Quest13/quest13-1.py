import copy


class Node:
    def __init__(self, level):
        self.level = level
        self.time = None
        self.adj = []

    def find_neighbors(self, row_idx, col_idx):
        if row_idx - 1 >= 0 and NODE_GRID[row_idx - 1][col_idx] != "#":
            self.adj.append(NODE_GRID[row_idx - 1][col_idx])
        if row_idx + 1 < len(NODE_GRID) and NODE_GRID[row_idx + 1][col_idx] != "#":
            self.adj.append(NODE_GRID[row_idx + 1][col_idx])
        if col_idx - 1 >= 0 and NODE_GRID[row_idx][col_idx - 1] != "#":
            self.adj.append(NODE_GRID[row_idx][col_idx - 1])
        if col_idx + 1 < len(NODE_GRID[0]) and NODE_GRID[row_idx][col_idx + 1] != "#":
            self.adj.append(NODE_GRID[row_idx][col_idx + 1])

    def traverse(self, run_time, visited):
        visited.append(self)
        if self.time is not None and run_time > self.time:
            return
        self.time = run_time
        if self == END_NODE:
            return
        for adj_node in self.adj:
            if adj_node not in visited:
                travel_time = abs(adj_node.level - self.level)
                if travel_time > 5:
                    travel_time = 10 - travel_time
                travel_time += 1
                adj_node.traverse(run_time + travel_time, visited.copy())


with open("quest13-1.txt", "r") as file:
    GRID = [list(row) for row in file.read().split("\n")]
    NODE_GRID = copy.deepcopy(GRID)
    for row_idx, row in enumerate(GRID):
        for col_idx, col in enumerate(row):
            if col == "#" or col == " ":
                continue
            elif col == "E":
                END_NODE = Node(0)
                NODE_GRID[row_idx][col_idx] = END_NODE
            elif col == "S":
                START_NODE = Node(0)
                START_NODE.time = 0
                NODE_GRID[row_idx][col_idx] = START_NODE
            else:
                NODE_GRID[row_idx][col_idx] = Node(int(col))

for row_idx in range(len(NODE_GRID)):
    for col_idx in range(len(NODE_GRID[0])):
        if NODE_GRID[row_idx][col_idx] not in ["#", " "]:
            NODE_GRID[row_idx][col_idx].find_neighbors(row_idx, col_idx)

START_NODE.traverse(0, [])
print(END_NODE.time)

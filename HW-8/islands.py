from collections import deque, defaultdict

def count_islands(grid):
  count = 0
  queue = deque()
  seen = set()
  
  for row_index, row in enumerate(grid):
    for col_index, cell in enumerate(row):
      if cell == "#" and (row_index, col_index) not in seen:
        queue.appendleft((row_index, col_index))
        seen.add((row_index, col_index))
        count += 1
        while queue:
          current = queue.pop()
          for neighbor in get_neighbors(current, grid):
            if neighbor not in seen:
              queue.appendleft(neighbor)
              seen.add(neighbor)
  return count

def get_neighbors(current, grid):
  neighbors = []
  moves = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
  ]
  
  for move in moves:
    cell = ((current[0] + move[0]), (current[1] + move[1]))
    if not is_within_scope(cell, grid):
      continue
    if grid[cell[0]][cell[1]] == "#":
      neighbors.append(cell)

  return neighbors

def is_within_scope(element, grid):
  try:
    if element[0] < 0 or element[1] < 0:
      raise Exception()
    grid[element[0]][element[1]]
  except:
    return False
  else:
    return True

'''print(count_islands(
[['~', '~', '#', '#'],
 ['~', '#', '#', '~'],
 ['#', '~', '~', '#'],
 ['~', '~', '#', '#']]
))'''
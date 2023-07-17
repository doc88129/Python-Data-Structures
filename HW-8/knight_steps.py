from collections import deque, defaultdict

def knight_steps(board, src, dst):
  connections = create_connections(board)
  queue = deque()
  seen = set()
  queue.appendleft((src, 0))
  seen.add(src)

  while queue:
    current, depth = queue.pop()
    if current == dst:
      return depth 
    for node in connections[current]:
      if node not in seen:
        seen.add(node)
        queue.appendleft((node, depth + 1))
  return -1

def create_connections(board):
  moves = [
    (1,2),
    (1,-2),  
    (-1,2),  
    (-1,-2),  
    (2,1),  
    (2,-1),  
    (-2,1),  
    (-2,-1)
  ]
  connections = defaultdict(list)
  
  for r in range(len(board)):
    for c in range(len(board[r])):
      if board[r][c] == 1:
        continue
      for move in moves:
        cell = (r + move[0], c + move[1])
        if not is_within_scope(cell, board):
          continue
        if board[cell[0]][cell[1]] == 0:
            connections[(r, c)].append(cell)
        
  return connections

def is_within_scope(element, grid):
  try:
    if element[0] < 0 or element[1] < 0:
      raise Exception()
    grid[element[0]][element[1]]
  except:
    return False
  else:
    return True

'''print(knight_steps([[0,0,0],   
               [0,0,0],   
               [0,0,0]], (2,0), (2,2)))
print(knight_steps([[0,1,0],   
               [0,0,0],   
               [0,0,0]], (2,0), (2,2)))'''
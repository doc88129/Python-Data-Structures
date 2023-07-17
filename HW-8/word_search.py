from collections import deque


def word_search(board, word):
  if word == "":
    return True 
  queue = deque();
  seen = set()

  for row_index, row in enumerate(board):
    for col_index, cell in enumerate(row):
      if cell == word[0]:
        queue.appendleft(((row_index, col_index),0))
        seen.add((row_index, col_index))

        while queue:
          current, depth = queue.pop()
          if depth >= len(word) - 1:
            return True 

          for neighbor in get_neighbors(current, board):
            if word[depth + 1] == board[neighbor[0]][neighbor[1]] and neighbor not in seen:
              queue.appendleft((neighbor, depth + 1))
              seen.add(neighbor)
  return False

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

'''print(word_search(
[['A','B','C','E'],    
['S','F','C','S'],    
['A','D','E','E']],

"ABCCED"
)) #True

print(word_search(
[['A','B','C','E'],    
['S','F','C','S'],    
['A','D','E','E']],

"SEE"
)) #True

print(word_search(
[['A','B','C','E'],    
['S','F','C','S'],    
['A','D','E','E']],

"ABCB"
)) #False'''
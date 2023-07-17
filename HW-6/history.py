from collections import deque


def history(clicks):
  path_taken = []
  history_past = deque()
  history_future = deque()
  for action in clicks:
    if action == '<':
      if len(history_past) > 1:
        tmp = history_past.pop()
        history_future.append(tmp)
        path_taken.append(history_past[-1])
    elif action == '>':
      if history_future:
        tmp = history_future.pop()
        history_past.append(tmp)
        path_taken.append(tmp)
    elif not history_past or action != history_past[-1]:
      history_past.append(action)
      path_taken.append(action)
      history_future.clear()
  return path_taken


assert history(
  ['Google', 'Facebook', 'Instagram', '<',
   '>']) == ['Google', 'Facebook', 'Instagram', 'Facebook', 'Instagram']

assert history([
  'Google', 'Facebook', 'Instagram', '<', '<', '>', 'Wikipedia', 'Reddit', '<',
  '<', '>'
]) == [
  'Google', 'Facebook', 'Instagram', 'Facebook', 'Google', 'Facebook',
  'Wikipedia', 'Reddit', 'Wikipedia', 'Facebook', 'Wikipedia'
]

assert history(
  ['Google', 'Instagram', 'Instagram', 'Wikipedia', '<',
   '<']) == ['Google', 'Instagram', 'Wikipedia', 'Instagram', 'Google']

assert history(['Google', 'Instagram', 'Reddit', 'Wikipedia', '<', 'Reddit'
                ]) == ['Google', 'Instagram', 'Reddit', 'Wikipedia', 'Reddit']

assert history(
  ['Google', 'Instagram', 'Reddit', 'Wikipedia', 'Reddit', '<', '<', '<']) == [
    'Google', 'Instagram', 'Reddit', 'Wikipedia', 'Reddit', 'Wikipedia',
    'Reddit', 'Instagram'
  ]

assert history(['Google', 'Facebook', '<',
                '<']) == ['Google', 'Facebook', 'Google']

assert history(['Google', 'Instagram', '<', 'Wikipedia',
                '>']) == ['Google', 'Instagram', 'Google', 'Wikipedia']

assert history(['Google', 'Instagram', '<', '<',
                '<']) == ['Google', 'Instagram', 'Google']

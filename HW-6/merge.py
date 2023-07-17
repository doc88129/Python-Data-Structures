from collections import deque


#version 2
def merge(nums):
  row = deque()
  for num in nums:
    while row and num == row[-1]:
      num *= 2
      row.pop()
    row.append(num)
  return list(row)


'''
print(merge([2, 2, 4, 4, 8, 8]))
print(merge([]))
print(merge([2]))
print(merge([2, 4]))
print(merge([2, 4, 2, 2, 2, 2]))
'''

'''
#version 1
def merge(nums):
  row = deque()
  for num in nums:
    if row and row[-1] == num:
      row.pop()
      row.append(num * 2)
      while len(row) > 1 and row[-2] == row[-1]:
        row.pop()
        num = row.pop()
        row.append(num * 2)
    else:
      row.append(num)
  return list(row)
'''

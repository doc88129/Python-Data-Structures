# Note: for unit tests to pass, you must return a new array
# and nums must remain unchanged.
def sort_squares(nums):
  lst = [n ** 2 for n in nums] #O(n)
  quicksort(lst, 0, len(nums) - 1) #avg: O(n)
  return lst

#Quick sort example from sorting replit
def partition(array, low, high):
  pivot = array[high]

  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      (array[i], array[j]) = (array[j], array[i])

  i += 1
  (array[i], array[high]) = (array[high], array[i])
  return i 
 
def quicksort(array, low, high):
  if low < high:
    pivot = partition(array, low, high)
    quicksort(array, low, pivot - 1) 
    quicksort(array, pivot + 1, high)

'''  
lst = [n ** 2 for n in nums]

  for i in range(1, len(lst) - 1):
    while i > 0 and lst[i - 1] > lst[i]:
      lst[i - 1], lst[i] = lst[i], lst[i - 1]
      i -= 1
  return lst
'''
#print(sort_squares([-3, -2, 0, 4, 6]))
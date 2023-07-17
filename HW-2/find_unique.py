from collections import defaultdict


def find_unique(nums):
  dic = defaultdict(int)
  for num in nums:  #O(n)
    dic[num] += 1
    #O(1)
  for key, value in dic.items():  #O(n)
    if value < 2:
      return key
  return None


print(find_unique([1, 4, 1, 3, 5, 5, 4]))
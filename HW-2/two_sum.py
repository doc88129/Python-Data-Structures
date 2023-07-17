def two_sum(nums, target):
  indices = set()
  for index, num in enumerate(nums):  #O(n)
    if (target - num) in nums[index + 1:]:  #O(n)
      indices.add(index)
      indices.add(nums.index(target - num, index + 1))  #O(n)
      return indices
  return indices


#print(two_sum([2, 7, 11, 15],9))
print(two_sum([1, 1, 1, 1, 1], 3))
#print(two_sum([],0))
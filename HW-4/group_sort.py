# Note: for unit tests to pass, this must be done in-place.
def group_sort(nums):
  for i in range(1, len(nums)):
    while i > 0 and nums[i - 1] > nums[i]:
      nums[i - 1], nums[i] = nums[i], nums[i - 1]
      i -= 1
  return nums

print(group_sort([2, 1, 1, 0, 2, 1]))
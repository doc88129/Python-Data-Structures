def circular_shift(nums, k):
  if len(nums) == 0:
    return nums
  nums.extend(nums[k % (len(nums)):] + nums[:k % (len(nums))])
  for _ in range(len(nums) // 2):
    nums.pop(0)
  return nums
  #return nums[k%(len(nums)):] + nums[:k%(len(nums))]

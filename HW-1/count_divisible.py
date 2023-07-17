def count_divisible(nums, k):
  count = 0
  for num in nums: #n
    if (num % k == 0):
      count += 1
  return count
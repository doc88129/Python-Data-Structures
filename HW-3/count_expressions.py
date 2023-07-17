def count_expressions(nums, target):
  if len(nums) == 0:
    return 0

  result = []
  count_help(nums, target, nums[0], result, 1)
  return len(result)


def count_help(nums, target, current, result, i):
  #print(current)
  if current == target and i != 1:
    result.append(current)
  if i >= len(nums):
    return

  count_help(nums, target, current + nums[i], result, i + 1)
  count_help(nums, target, current - nums[i], result, i + 1)
  count_help(nums, target, current * nums[i], result, i + 1)


'''
print(count_expressions([1,2,3], 6))
print(count_expressions([1,2,5], 7))

print(count_expressions([], 0))
'''
#print(count_expressions([0,0,0], 0))

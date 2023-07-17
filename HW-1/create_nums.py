def create_nums(s):
  useable_nums = [i for i in range(len(s)+1)]
  nums = []

  for char in s:
    if char == "I":
      num = min(useable_nums)
      nums.append(num)
      useable_nums.remove(num)
    elif char == "D":
      num = max(useable_nums)
      nums.append(num)
      useable_nums.remove(num)
    if len(useable_nums) == 1:
      nums.extend(useable_nums)
  return nums
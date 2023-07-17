def can_divide(nums):

  def helper(nums1, nums2): #n
    if nums1 == []:
      return False
    if sum(nums1) == sum(nums2): #2n
      return True
    tmp = nums1.pop()
    nums2.append(tmp)
    return helper(nums1, nums2)

  if len(nums) < 2:
    return True

  nums1 = [i for i in nums if i % 5 != 0] #n
  nums2 = [i for i in nums if i % 5 == 0] #n
  return helper(nums1, nums2)


'''
print(can_divide([4, 4]))  #TRUE
print(can_divide([2, 2, 2]))  #FALSE
print(can_divide([5, 2, 3]))  #TRUE
print(can_divide([0]))  #TRUE
'''
def gen_subsets(nums):
  results = []

  def gen_helper(nums):
    #if nums not in results:
    results.append(nums)

    for i in range(len(nums)):
      tmp = nums.pop(i)
      gen_helper(nums[:])
      nums.insert(i, tmp)

  gen_helper(nums)

  seen = []
  for i in results:
    if i not in seen:
      seen.append(i)
  return seen


#print(gen_subsets([1,2]))


# This function is just here to help you write unit tests.
# Feel free to use it, but you don't need to.
# Checks if two lists of lists contain the
# same subsets regardless of the order they appear
def same_subsets(lst1, lst2):
  if len(lst1) != len(lst2):
    return False

  set1 = set()
  for e1 in lst1:
    set1.add(tuple(sorted(e1)))

  set2 = set()

  for e2 in lst2:
    set2.add(tuple(sorted(e2)))

  return set1 == set2

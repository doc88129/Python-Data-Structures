from tree_node import TreeNode

def range_count(root, min_val, max_val):
  if not root:
    return 0

  left_right_count = range_count(root.left, min_val, max_val) + range_count(root.right, min_val, max_val)
  if root.val > min_val and root.val < max_val:
    return 1 + left_right_count
  return left_right_count

'''
root = TreeNode(7, TreeNode(10, TreeNode(12), TreeNode(9)), TreeNode(3, TreeNode(5), TreeNode(-1)))
print(range_count(root, 2, 10)) #4
print(range_count(root, 3, 8)) #2
print(range_count(root, 10, 20)) #1
print(range_count(root, 20, 30)) #0
print(range_count(None, 20, 30)) #0
print(range_count(TreeNode(25), 20, 30)) #1
'''
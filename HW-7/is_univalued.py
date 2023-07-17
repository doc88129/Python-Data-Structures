from tree_node import TreeNode


def is_univalued(root):
  if not root:
    return True

  def helper(root, value):
    if not root:
      return True
    if root.val != value:
      return False
    
    return helper(root.right, value) and helper(root.left, value)

  return helper(root, root.val)


'''
root = TreeNode(5, TreeNode(5), TreeNode(5))
print(is_univalued(root))
root = TreeNode(5, TreeNode(4), TreeNode(5))
print(is_univalued(root))
root = TreeNode(5)
print(is_univalued(root))
root = None
print(is_univalued(root))
'''

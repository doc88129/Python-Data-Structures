class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)
    
def pretty_print(root, depth=0):
  """helper method prints out the tree oriented horizontally, a 90 degree
     rotation from the usual top-down view."""
  if not root:
    return
  pretty_print(root.right, depth + 1)
  print(depth * "   " + str(root.val))
  pretty_print(root.left, depth + 1)
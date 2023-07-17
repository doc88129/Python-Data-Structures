from tree_node import TreeNode, pretty_print


def invert(root):
  if not root:
    return

  root.right, root.left = root.left, root.right
  invert(root.right)
  invert(root.left)
  return root

'''
Test cases
'''
root = TreeNode(7, TreeNode(10, TreeNode(12), TreeNode(9)),
                TreeNode(3, TreeNode(5), TreeNode(-1)))
pretty_print(root)
print("===========")
invert(root)
pretty_print(root)
print("===========")
#pretty_print(TreeNode(7, TreeNode(3, TreeNode(-1), TreeNode(5)), TreeNode(10, TreeNode(9), TreeNode(12))))
#assert root == TreeNode(7, TreeNode(3, TreeNode(-1), TreeNode(5)), TreeNode(10, TreeNode(9), TreeNode(12)))

print("=======================")
root = TreeNode(2, TreeNode(3), TreeNode(1))
pretty_print(root)
print("===========")
invert(root)
pretty_print(root)

print("=======================")
root = TreeNode(7, TreeNode(10, TreeNode(12), TreeNode(9)), TreeNode(3))
pretty_print(root)
print("===========")
invert(root)
pretty_print(root)

print("=======================")
root = TreeNode(7, TreeNode(10, TreeNode(12)))
pretty_print(root)
print("===========")
invert(root)
pretty_print(root)

print("=======================")
root = TreeNode(7, TreeNode(10, TreeNode(12)),
                TreeNode(12, None, TreeNode(11, TreeNode(9))))
pretty_print(root)
print("===========")
invert(root)
pretty_print(root)

print("=======================")
root = TreeNode(7)
pretty_print(root)
print("===========")
invert(root)
pretty_print(root)

print("=======================")
root = None
pretty_print(root)
print("===========")
invert(root)
pretty_print(root)

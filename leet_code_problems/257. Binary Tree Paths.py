# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    ans = []

    if not root.left and not root.right :
        return [str(root.val)]

    def helper(node,curr_path):
      if not node:
        return
      if not node.left and not node.right :
        ans.append("".join(curr_path)+str(node.val))
        return
      if node:
        curr_path.append(str(node.val)+"->")

      helper(node.left,curr_path)
      helper(node.right,curr_path)
      curr_path.pop()

    helper(root,[])

    return ans







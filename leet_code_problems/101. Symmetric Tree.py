# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True

        path1 = root.left
        path2 = root.right
        def checker(path1,path2):
            if not path1 and not path2:
                return True
                
            if path1 and path2 and path1.val == path2.val :
                return checker(path1.left,path2.right) and checker(path1.right,path2.left)
            else:
                return False

        return checker(path1,path2)

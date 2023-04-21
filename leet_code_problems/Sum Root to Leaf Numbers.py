# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.ans=0
        def dfs(node,curr_sum):
            
            if not node:
                return
            curr_sum+=str(node.val)
            if not node.left and not node.right:
                self.ans+=int(curr_sum)
                
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
            curr_sum=curr_sum[:-1]
            
          
        dfs(root,"")

        return self.ans

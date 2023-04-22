# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found=0
        def dfs(node,curr_sum):
           
            if not node:
                return
            curr_sum+=node.val
            if node.left==None and node.right==None and (curr_sum==targetSum):
                self.found=1

            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
            curr_sum-=node.val
            
        dfs(root,0)

        return self.found==1

        

       
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        stack=""
        def dfs(node):
            nonlocal stack
            if not node:
                return
            if not node.left and not node.right:
                stack+="("+str(node.val)+")"
                return
            stack+="("+str(node.val)    
            if not node.left:
                stack+="()"
                  
            dfs(node.left)
            dfs(node.right)
            stack+=")"
        
        dfs(root)

        return stack[1:-1]

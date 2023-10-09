# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = 0
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def find(node, comb):
            if not node:
                return
            
            comb.append(node.val)
            
            if sum(comb) == targetSum and not node.left and not node.right:
                ans.append(comb.copy())
            
            find(node.left, comb)
            find(node.right, comb)
           
            comb.pop()
        
        find(root, [])
        
        return ans

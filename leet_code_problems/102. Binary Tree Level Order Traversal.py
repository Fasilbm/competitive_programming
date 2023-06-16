# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        ans = []
        while queue:
            res = []
            size = len(queue)
            for i in range(size):
                num = queue.popleft()
                if num.left:
                    queue.append(num.left)
                if num.right:
                    queue.append(num.right)
                res.append(num.val)
            ans.append(res)
            
        return (ans)
                



        

        

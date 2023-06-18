# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            res.append(queue[0].val)
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp.right:
                    queue.append(tmp.right)
                if tmp.left:
                    queue.append(tmp.left)
        return res




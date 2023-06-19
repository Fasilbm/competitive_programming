# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        nums = []
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size): 
                node = queue.popleft()
                nums.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        nums.sort()
        return nums[k-1]
                

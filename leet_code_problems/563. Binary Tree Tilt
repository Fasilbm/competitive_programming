# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.tilt=0

        if not root or not root.left and not root.right :
            return 0

        def helper(root,left_sum,right_sum,tilt):

            if not root:
              return 0
            left_sum=helper(root.left,left_sum,right_sum,tilt)
            right_sum=helper(root.right,left_sum,right_sum,tilt)

            self.tilt+=abs(left_sum-right_sum)
            print(tilt)

            return left_sum+right_sum+root.val

        helper(root,0,0,self.tilt)

        return self.tilt

     

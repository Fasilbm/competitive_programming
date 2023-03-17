# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        counter = defaultdict(int)
        counter[0]=1
        self.count = 0

        def find_candidate(node,targetSum,curr_prefix):

            if not node:
                return

            curr_prefix += node.val
            self.count+=counter[curr_prefix-targetSum]
            counter[curr_prefix]+=1
          
            find_candidate(node.left,targetSum,curr_prefix)
            find_candidate(node.right,targetSum,curr_prefix)
            counter[curr_prefix]-=1
            curr_prefix -= node.val

        find_candidate(root,targetSum,0)

        return self.count

            

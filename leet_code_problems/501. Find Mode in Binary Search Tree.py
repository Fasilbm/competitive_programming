# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = defaultdict(int)
        def helper(node):

            if node:
                ans[node.val] += 1
                helper(node.left)
                helper(node.right)
            else:
                return

        helper(root)
        res =[]
        ans={k: v for k, v in sorted(ans.items(), key=lambda item: -item[1])}

        for i,j in ans.items():

            if not res:
                res.append(i)
            elif ans[res[-1]] == ans[i]:
                res.append(i)
            else:
                break
        return (res)




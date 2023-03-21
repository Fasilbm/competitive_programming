# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter=defaultdict(int)
        ans=[]

        if not root.left and not root.right:

            return [root.val]

        def helper(root,left_sum,right_sum,_sum):

            if not root:
                return 0
            
            left_sum=helper(root.left,left_sum,right_sum,_sum)
            right_sum=helper(root.right,left_sum,right_sum,_sum)
            _sum = left_sum + right_sum + root.val
            counter[_sum]+=1
            return _sum

        helper(root,0,0,0)

        counter={k:v for k,v in sorted(counter.items(),key=lambda items:-items[1])}
        print(counter)

        for i,j in counter.items():

            if not ans:
                ans.append(i)
            if counter[ans[-1]]>j:
                return ans[1:]
            else:
                ans.append(i)
        return (ans[1:])


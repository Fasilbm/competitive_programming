"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        self.max_depth=0
        def dfs(node,current_depth,max_depth):
            if node==None:
                return
            current_depth+=1
            self.max_depth=max(self.max_depth,current_depth)
            for node in node.children:
                dfs(node,current_depth,self.max_depth)

        dfs(root,0,0)

        return self.max_depth

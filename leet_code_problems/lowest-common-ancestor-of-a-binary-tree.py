# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        adj_list = {root.val:root.val}
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                can = queue.popleft()
                if can.left:
                    adj_list[can.left.val] = can.val
                    queue.append(can.left)
                if can.right:
                    adj_list[can.right.val] = can.val
                    queue.append(can.right)
        ps = []
        qs = []
        a = p.val
        while True:
            if adj_list[a] != root.val:
                ps.append(adj_list[a])
                a = adj_list[a]
            else:
                ps.append(root.val)
                break
        b = q.val
        while True:
            if adj_list[b] != root.val:
                qs.append(adj_list[b])
                b = adj_list[b]
            else:
                qs.append(root.val)
                break
        x = 0
        found = 0
        for i in ps:
            if i == q.val:
                x = i
                found =1
                break
            elif i in qs:
                x = i
                break
        if not found:
            for i in qs:
                if i == p.val:
                    x = i
                    break
                elif i in ps:
                    x = i
                    break
        print(x)
        queue=deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                can = queue.popleft()
                if can.val == x:
                    return can
                if can.left:
                    if can.val==x:
                        return can.left
                    queue.append(can.left)
                if can.right:
                    if can.val==x:
                        return can.right
                    queue.append(can.right)
            
                


        

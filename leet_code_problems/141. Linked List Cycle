# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        flag=10**6
        while head:
            if head.val==flag:
                return True
            else:
                head.val=flag
            head=head.next
        return False
        






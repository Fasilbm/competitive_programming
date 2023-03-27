# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> int:

        tracker=[]
        while head:
            if head in tracker:
               return head
            tracker.append(head)
            head=head.next
        return None

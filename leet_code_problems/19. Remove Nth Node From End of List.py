# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count=0
        curr=head
        while curr!=None:
            count+=1
            curr=curr.next
        pos=count-n
        new_Count=1
        curr=head
        if pos==0:
            return head.next
        while curr!=None:
            if new_Count==pos:
                curr.next=curr.next.next
                return head
           
            new_Count+=1
            curr=curr.next



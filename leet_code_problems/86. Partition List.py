# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=ListNode()
        greater=ListNode()
        less_ptr=less
        greater_ptr=greater

        while head!=None:

            if head.val>=x:
                greater_ptr.next=head
                greater_ptr=greater_ptr.next
            else:
                less_ptr.next=head
                less_ptr=less_ptr.next
              
                
            head=head.next

        less_ptr.next=greater.next
        greater_ptr.next=None
        
        return less.next



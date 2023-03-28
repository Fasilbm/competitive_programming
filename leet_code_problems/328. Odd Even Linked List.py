# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        odd_list=head
        even_list=head.next
        merge=even_list

        while even_list and even_list.next:
           odd_list.next=even_list.next
           odd_list=odd_list.next
           even_list.next=odd_list.next
           even_list=even_list.next

        odd_list.next=merge

        return head






    

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

       dummy=ListNode()
       curr=dummy
       n1,n2="",""
       while l1:
           n1=str(l1.val)+n1
           l1=l1.next
       while l2:
           n2=str(l2.val)+n2
           l2=l2.next
       if not n1: n1="0"
       if not n2:n2="0"
       sum=int(n1)+int(n2)
       for i in reversed(str(sum)):
           curr.next=ListNode(int(i))
           curr=curr.next
       return dummy.next
    
#Time complexity max O(n,m) where n,m are length of the linked list
#space complexity max O(n,m) where n,m are length of the linked list

        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list=[]
        while head:
            list.append(head.val)
            head=head.next
        
        h=0
        t=len(list)
        while h<=t:
            if list[h]!=list[t-1]:
                return False
            h+=1
            t-=1
        return True
        

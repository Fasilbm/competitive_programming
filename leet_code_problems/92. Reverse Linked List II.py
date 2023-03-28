# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        arr=[]
        left-=1
        right-=1
        while head:
            arr.append(head.val)
            head=head.next
        
        rev=arr[left:right+1]
        ans=arr[:left]+rev[::-1]+arr[right+1:]

        new=ListNode()
        cur=new
        for i in range(len(ans)):
            temp=ListNode(ans[i])
            cur.next=temp
            cur=cur.next
        return new.next


        
        


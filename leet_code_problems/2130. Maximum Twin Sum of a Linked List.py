# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        sum_=0
        for i,j in enumerate(arr):
            if 0<=i<=(len(arr)/2)-1:
                sum_=max(sum_,(arr[i]+arr[len(arr)-1-i]))

        return sum_

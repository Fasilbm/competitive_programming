# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        while (list1!=None and list2!=None):
            if (list1.val<list2.val):
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
       
        if(list1!=None):
                curr.next=list1
            
        if(list2!=None):
                curr.next=list2
               
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        self.dummy= ListNode()

        self.curr = self.dummy


        def helper(list1,list2):

            if not list1:

                self.curr.next = list2


            if not list2:

                self.curr.next = list1


            if list1 and list2 :

                if list1.val > list2.val :

                    self.curr.next = ListNode(list2.val)

                    list2 = list2.next

                    self.curr = self.curr.next

                    helper(list1,list2)

                else:

                    self.curr.next = ListNode(list1.val)

                    list1= list1.next

                    self.curr = self.curr.next

                    helper(list1,list2)

        helper(list1,list2)

        return self.dummy.next

         

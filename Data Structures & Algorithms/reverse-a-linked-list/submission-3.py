# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr: # goes until end of linked list
            temp = curr.next; # save pointer to next node
            curr.next = prev
            prev = curr
            curr = temp
    
        return prev # not curr, since it is null.
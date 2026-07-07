# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head: # breaks when null
            if (not head.val):
                return True
            head.val = None # setting to null, so that we can see later
            head = head.next
        return False
        
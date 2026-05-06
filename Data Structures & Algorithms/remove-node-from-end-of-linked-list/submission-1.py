# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        trav = head
        while trav:
            trav = trav.next
            length += 1
        prev = None
        trav = head
        index = length - n
        for i in range(index):
            prev = trav
            trav = trav.next
        if length <= 1:
            return None
        # at start of list
        if not prev:
            head = head.next
        else:
            prev.next = trav.next
            trav.next = None
        return head
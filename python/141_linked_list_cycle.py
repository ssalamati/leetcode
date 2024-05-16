# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                return True

        return False

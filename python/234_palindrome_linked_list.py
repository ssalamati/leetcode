# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = fast = head
        prev = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next

            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        if fast is not None:
            slow = slow.next

        while slow and prev:
            if prev.val != slow.val:
                return False
            slow = slow.next
            prev = prev.next

        return not slow and not prev

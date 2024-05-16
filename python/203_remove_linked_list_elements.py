# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = dummy = ListNode(val=0, next=head)
        cur = head

        while cur is not None:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# This solution takes 28ms and beats 96.03% of users
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            current.next.val, current.val = current.val, current.next.val
            current = current.next.next
        return head
        
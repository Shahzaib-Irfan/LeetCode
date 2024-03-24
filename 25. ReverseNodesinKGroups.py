# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This solution takes 24ms and beats 99.94% of users.
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes_count = 0
        current = head
        while current:
            nodes_count += 1
            current = current.next
        
        def recurse(head, k, size):
            if size < k:
                return head
            
            if head is None:
                return None
            
            current = head
            prev = None
            nxt = None
            count = 0
            while current and count < k:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
                count += 1
            head.next = recurse(nxt, k, size - k)
            return prev
        return recurse(head, k, nodes_count)
        
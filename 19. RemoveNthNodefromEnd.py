# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This solution takes 30ms and beats 96.03% of users
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        list1 = []
        total_nodes = 0
        while current:
            total_nodes += 1
            list1.append(current.val)
            current = current.next
        current = head
        count = 1
        prev = None

        while current:
            if count + n - 1 == len(list1):
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
                return head
            count += 1
            prev = current
            current = current.next

        return head

        
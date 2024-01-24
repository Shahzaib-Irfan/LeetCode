# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def merge(list1, list2):
            sentinel = ListNode()
            current = sentinel

            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            
            current.next = list1 or list2
            
            return sentinel.next

        if not lists:
            return None

        sortedLists = lists[0]

        for i in range(1, len(lists)):
            sortedLists = merge(sortedLists, lists[i])

        return sortedLists
        
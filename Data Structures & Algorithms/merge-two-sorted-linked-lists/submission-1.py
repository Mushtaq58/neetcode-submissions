# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        start1 = list1
        start2 = list2

        dummy = ListNode()
        current = dummy

        while start1 is not None and start2 is not None:
            if start1.val <= start2.val:
                current.next = start1
                start1 = start1.next
            else:
                current.next = start2
                start2 = start2.next

            current = current.next

        if start1 is None:
            current.next = start2
        elif start2 is None:
            current.next = start1

        return dummy.next
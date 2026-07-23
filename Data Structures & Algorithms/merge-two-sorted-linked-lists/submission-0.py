# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            elif list1.val > list2.val:
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
            else:  # list1.val == list2.val
                # Insert from list1
                current.next = ListNode(list1.val)
                current = current.next
                # Insert from list2
                current.next = ListNode(list2.val)
                current = current.next
                # Advance both pointers
                list1 = list1.next
                list2 = list2.next

        # Append remaining nodes from list1
        while list1:
            current.next = ListNode(list1.val)
            current = current.next
            list1 = list1.next

        # Append remaining nodes from list2
        while list2:
            current.next = ListNode(list2.val)
            current = current.next
            list2 = list2.next

        return dummy.next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None             # 🪐 1️⃣ Initially, no nodes have been reversed
        curr = head             # 🪐 2️⃣ Start at the head of the list

        while curr:
            next_node = curr.next   # 🪐 3️⃣ Save the next node before reversing

            curr.next = prev        # 🪐 4️⃣ Reverse the pointer

            prev = curr             # 🪐 5️⃣ Move prev forward to the current node
            curr = next_node        # 🪐 6️⃣ Move curr forward to the saved next node

        return prev    
        
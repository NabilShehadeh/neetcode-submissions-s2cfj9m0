# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. intialize prev and curr pointers, with None and Head, since while curr is none we're iterating
        # 2. setup a while loop to keep on iterating.
        # 3. nxt -> curr.next -> prev -> curr -> nxt # that way we change the direction of the arrows.
        # 4. return the prev, since that becomes the new head. 
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev # here we have the reverse arrow switch.
            prev = curr
            curr = nxt # here its none and we reach the end of the list
        return prev
        
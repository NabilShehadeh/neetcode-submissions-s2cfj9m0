# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. first we're going to intialize the curr, head
        # 2. we'll setup a while loop while curr is not none, since that means we can still iterate.
        # 3. we'll have nxt a temporary pointer point to curr.next -> prev 
        # 4. prev -> curr, curr -> nxt , here we reach none and complete the iteration.
        # 5. return prev since that is the nead head. 

        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev # here we switch around the arrow direction.
            prev = curr
            curr = nxt # the temporary variable.
        return prev
        
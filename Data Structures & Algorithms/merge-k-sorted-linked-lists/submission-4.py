# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # collecting the nodes and sorting them 
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        # dummy headers
        res = ListNode(0)
        cur = res

        #going throughn the nodes again
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next
        
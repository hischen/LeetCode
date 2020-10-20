# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        A=headA
        B=headB
        while A!=B:
            if A==None:
                A=headB
            else:
                A=A.next
            if B==None:
                B=headA
            else:
                B=B.next
        return A

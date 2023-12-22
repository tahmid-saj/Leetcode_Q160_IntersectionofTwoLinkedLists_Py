# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None: return None

        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            if nodeA == None: nodeA = headB
            else: nodeA = nodeA.next
            if nodeB == None: nodeB = headA
            else: nodeB = nodeB.next

        return nodeA

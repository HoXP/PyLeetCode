# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        ret = ListNode(-1)
        root = ret
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                ret.next = l1
                ret = l1
                l1 = l1.next
            else:
                ret.next = l2
                ret = l2
                l2 = l2.next
        if l1 != None:
            ret.next = l1
        if l2 != None:
            ret.next = l2
        return root.next

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
a = s.mergeTwoLists(l1, l2)
t = a
while t:
    print(t.val)
    t = t.next
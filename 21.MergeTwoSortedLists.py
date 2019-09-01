class ListNode(object):  
    def __init__(self):  
        self.val = None  
        self.next = None  

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    print(mergeTwoLists([1,2,4],[1,3,4]))
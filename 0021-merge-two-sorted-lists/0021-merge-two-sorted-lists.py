# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        elif l1 is not None and l2 is None:
            return l1
        elif l1 is None and l2 is not None:
            return l2
        
        if l1.val <= l2.val:
            l = ListNode(l1.val)
            ans = l
            l1 = l1.next
        else:
            l = ListNode(l2.val)
            ans = l
            l2 = l2.next
            
        while l1 is not None or l2 is not None:
            if l1 is not None:
                if l2 is not None:
                    if l1.val <= l2.val:
                        l.next = ListNode(l1.val)
                        l = l.next
                        l1 = l1.next
                    else:
                        l.next = ListNode(l2.val)
                        l = l.next
                        l2 = l2.next
                else:
                    l.next = ListNode(l1.val)
                    l = l.next
                    l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l = l.next
                l2 = l2.next
        return ans

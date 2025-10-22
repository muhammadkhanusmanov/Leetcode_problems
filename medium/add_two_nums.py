# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def add_node(curr, new_v):
    b = ListNode(new_v)
    if not curr:
        return b
    a = curr
    while a.next:
        a = a.next
    a.next = ListNode(new_v)
    return curr

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        q=0
        b = l1.val+l2.val
        a = ListNode(b%10)
        q=b//10
        l1 = l1.next
        l2 = l2.next
        while not (l1==None and l2==None):
            if (l1!=None and l2==None):
                l2 = add_node(l2,0)
            elif (l1==None and l2!=None):
                l1 = add_node(l1,0)
            b = l1.val + l2.val
            a = add_node(a, (b+q)%10)
            q = (b+q)//10
            l1 = l1.next
            l2 = l2.next
            
        if q==1:
            return add_node(a,1)
        else:
            return a
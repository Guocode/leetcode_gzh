# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nid = 1
        tmp = head
        while tmp.next:
            tmp = tmp.next
            nid+=1
        tmp = head
        prev = None
        # prev = head
        # tail = prev.next
        for i in range(nid-n):
            prev = tmp
            tmp = tmp.next
        if prev:
            prev.next = tmp.next
        else:
            return tmp.next
        return head

if __name__ == '__main__':
    head= ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,)))))
    a = Solution().removeNthFromEnd(head,2)
    # head= ListNode(1,ListNode(2,))
    # a = Solution().removeNthFromEnd(head,2)
    while a:
        print(a.val)
        a = a.next
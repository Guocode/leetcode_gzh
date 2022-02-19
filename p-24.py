# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        h = ListNode(-1)
        h.next = head

        leftleft = h
        left = head
        right = head.next

        while left and right:
            leftleft.next = right
            left.next = right.next
            right.next = left

            leftleft = left
            left = leftleft.next
            if not left:
                break
            right = left.next
            if not right:
                break
        return h.next

if __name__ == '__main__':
    x = ListNode(1,ListNode(2,ListNode(3,)))
    y = Solution().swapPairs(x)
    while y:
        print(y.val)
        y = y.next
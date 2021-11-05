# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     ans = ListNode()
    #     stpval = 0
    #     tmp = ans
    #     while 1:
    #         if l1 is None and l2 is None and stpval==0:
    #             break
    #
    #         l1v = l1.val if l1 is not None else 0#
    #         l2v = l2.val if l2 is not None else 0
    #
    #         curval = (l1v + l2v + stpval) % 10
    #         stpval = (l1v + l2v + stpval) // 10
    #
    #         tmp.val = curval
    #
    #         l1 = l1.next if l1 is not None else None#
    #         l2 = l2.next if l2 is not None else None#
    #         if l1 is None and l2 is None and stpval==0:
    #             break
    #         tmp.next = ListNode()
    #         tmp = tmp.next
    #     return ans
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        stpval = 0
        while 1:
            if l1 is None and l2 is None and stpval==0:
                break

            l1v = l1.val if l1 is not None else 0#
            l2v = l2.val if l2 is not None else 0

            curval = (l1v + l2v + stpval) % 10
            stpval = (l1v + l2v + stpval) // 10

            if head is None:
                head = ListNode(curval)
                tail = head
            else:
                tail.next = ListNode(curval)
                tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head


if __name__ == '__main__':
    a = ListNode(2, ListNode(4, ListNode(3, )))
    b = ListNode(5, ListNode(6, ListNode(4, )))

    c = Solution.addTwoNumbers(None, a, b)
    while c is not None:
        print(c.val)
        c = c.next

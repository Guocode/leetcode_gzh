# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.mergeKd2Lists(lists[:len(lists) // 2], lists[len(lists) // 2:])[0]

    def mergeKd2Lists(self, l1s, l2s):
        if len(l1s) > 1:
            l1s = self.mergeKd2Lists(l1s[:len(l1s) // 2], l1s[len(l1s) // 2:])
        if len(l2s) > 1:
            l2s = self.mergeKd2Lists(l2s[:len(l2s) // 2], l2s[len(l2s) // 2:])
        if len(l1s)==0:
            return l2s
        elif len(l2s)==0:
            return l1s
        return [self.merge2Lists(l1s[0],l2s[0])]

    def merge2Lists(self, l1, l2):
        ret = ListNode(-1)
        tmp = ret
        aptr = l1
        bptr = l2
        while True:
            if aptr is None and bptr is None:
                break
            if aptr is None and bptr is not None:
                tmp.next = bptr
                bptr = bptr.next
            if bptr is None and aptr is not None:
                tmp.next = aptr
                aptr = aptr.next
            if bptr is not None and aptr is not None:
                if aptr.val < bptr.val:
                    tmp.next = aptr
                    aptr = aptr.next
                else:
                    tmp.next = bptr
                    bptr = bptr.next
            tmp = tmp.next
        return ret.next


if __name__ == '__main__':
    x = [ListNode(1, ListNode(4, ListNode(5, ))), ListNode(1, ListNode(3, ListNode(4, ))), ListNode(2, ListNode(6, ))]
    y = Solution().mergeKLists([])
    while y is not None:
        print(y.val)
        y = y.next

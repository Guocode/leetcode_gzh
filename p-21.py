class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        ans = None
        tmp = None
        while head1 is not None or head2 is not None:
            if head1 is None:
                if ans is None:
                    ans = head2
                    tmp = ans
                else:
                    tmp.next = head2
                    tmp = tmp.next
                head2 = head2.next
                continue
            elif head2 is None:
                if ans is None:
                    ans = head1
                    tmp = ans
                else:
                    tmp.next = head1
                    tmp = tmp.next
                head1 = head1.next
                continue

            if head1.val < head2.val:
                if ans is None:
                    ans = head1
                    tmp = ans
                else:
                    tmp.next = head1
                    tmp = tmp.next
                head1 = head1.next

            else:
                if ans is None:
                    ans = head2
                    tmp = ans
                else:
                    tmp.next = head2
                    tmp = tmp.next
                head2 = head2.next

        return ans
if __name__ == '__main__':
    # a = ListNode(1,ListNode(2,ListNode(4,)))
    # b =  ListNode(1,ListNode(3,ListNode(4,)))
    a = None
    b =  ListNode(1,ListNode(3,ListNode(4,)))
    x = Solution().mergeTwoLists(a,b)
    while x:
        print(x.val)
        x = x.next
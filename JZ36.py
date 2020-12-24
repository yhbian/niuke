

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        while pHead1 is not None:
            pHead2_ = pHead2
            while pHead2_ is not None:
                if pHead1 == pHead2_:
                    return pHead1
                pHead2_ = pHead2_.next
            pHead1 = pHead1.next


if __name__ == '__main__':
    pHead1 = ListNode(x=1)
    pHead1.next = ListNode(x=2)
    pHead1.next.next = ListNode(x=3)

    pHead2 = ListNode(x=1)
    pHead2.next = pHead1.next

    common_node = Solution().FindFirstCommonNode(pHead1=pHead1, pHead2=pHead2)
    print(common_node.val)

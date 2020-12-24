class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        pre_node = []
        while pHead is not None:
            pre_node.append(pHead)
            if pHead.next in pre_node:
                return pHead.next  # note the definition of 'entry node'
            else:
                pHead = pHead.next
        return None


if __name__ == '__main__':
    pHead = ListNode(x=1)
    pHead.next = ListNode(x=2)
    pHead.next.next = ListNode(x=3)
    pHead.next.next.next = pHead.next
    print(Solution().EntryNodeOfLoop(pHead=pHead).val)

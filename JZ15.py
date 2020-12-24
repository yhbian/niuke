# -*- coding:utf-8 -*-
from LinkList import _construct_link, _visualize_link


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return pHead

        if not pHead.next:
            return pHead

        original_lst = []
        while pHead is not None:
            original_lst.append(pHead.val)
            pHead = pHead.next

        reversed_lst = list(reversed(original_lst))
        next_node = ListNode(reversed_lst[-1])
        node = None
        for i in range(1, len(reversed_lst)):
            node = ListNode(reversed_lst[-i-1])
            node.next = next_node
            next_node = node
        return node


if __name__ == '__main__':
    pHead = _construct_link([])
    solution = Solution()
    _visualize_link(solution.ReverseList(pHead))

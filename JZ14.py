# -*- coding:utf-8 -*-
import LinkList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None
        if not k:
            return None
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        if len(lst) < k:
            return None
        lst = lst[-k:]
        next_node = ListNode(lst[-1])
        node = next_node
        for i in range(1, len(lst)):
            node = ListNode(lst[-1-i])
            node.next = next_node
            next_node = node
        return node


if __name__ == '__main__':
    solution = Solution()
    head = LinkList._construct_link([1, 2, 3, 4, 5])

    k = 1
    LinkList._visualize_link(solution.FindKthToTail(head, k))

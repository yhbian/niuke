# -*- coding:utf-8 -*-
from LinkList import _visualize_link, _construct_link

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here

        if not pHead1 and not pHead2:
            return None
        # link2list
        lst1 = []
        lst2 = []
        while pHead1 is not None:
            lst1.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2 is not None:
            lst2.append(pHead2.val)
            pHead2 = pHead2.next
        merged_lst = sorted(lst1 + lst2)

        # list2link
        next_node = ListNode(merged_lst[-1])
        if len(merged_lst) == 1:
            node = next_node
        for i in range(1, len(merged_lst)):
            node = ListNode(merged_lst[-1-i])
            node.next = next_node
            next_node = node
        return node


if __name__ == '__main__':
    pHead1 = _construct_link([])
    pHead2 = _construct_link([1])
    solution = Solution()
    _visualize_link(solution.Merge(pHead1, pHead2))

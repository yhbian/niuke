# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return
        cloned = RandomListNode(x=pHead.label)
        cloned.random = pHead.random
        cloned.next = self.Clone(pHead=pHead.next)
        return cloned

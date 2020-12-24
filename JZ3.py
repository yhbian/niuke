# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        lst = []
        if not listNode:
            return lst
        while listNode.next is not None:
            lst.append(listNode.val)
            listNode = listNode.next
        lst.append(listNode.val)
        return list(reversed(lst))


class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    """
    A stack is constructed when recursion uses a function itself. i.e. It returns a function to the top of the stack

    """
    def __init__(self):
        self.lst = []

    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        self.lst.append(listNode.val)
        if listNode.next is not None:
            return self.printListFromTailToHead(listNode.next)
        else:
            return list(reversed(self.lst))


if __name__ == '__main__':
    solution2 = Solution2()
    listNode = ListNode(64)
    listNode2 = ListNode(32)
    listNode.next = listNode2
    result = solution2.printListFromTailToHead(listNode=listNode)
    print(result)



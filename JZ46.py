# -*- coding:utf-8 -*-
class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def construct(self, n):
        head = self.ListNode(x=0)
        node = head
        for i in range(1, n):
            node.next = self.ListNode(i)
            node = node.next
        node.val = n-1
        node.next = head
        return head

    def delete_node(self, head, val):
        # delete the first node with given val
        node = head
        while 1:
            if node.next.val == val:
                node.next = node.next.next
                break
            node = node.next
        return node.next

    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n:
            return -1
        if n == 1:
            return 0
        node = self.construct(n=n)
        while node.val != node.next.val:
            for i in range(m-1):
                node = node.next
            val = node.val
            node = self.delete_node(head=node, val=val)
        return node.val


if __name__ == '__main__':
    print(Solution().LastRemaining_Solution(n=5, m=3))


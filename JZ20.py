# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []

    def push(self, node):
        # write code here
        return self.stack.append(node)

    def pop(self):
        # write code here
        if not self.stack:
            raise
        return self.stack.pop()

    def top(self):
        # write code here
        if not self.stack:
            raise
        return self.stack[-1]

    def min(self):
        # write code here
        if not self.stack:
            raise
        return min(self.stack)

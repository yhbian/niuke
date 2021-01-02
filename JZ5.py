# -*- coding:utf-8 -*-


class TrickSolution:
    def __init__(self):
        self.queue = []

    def push(self, node):
        # write code here
        self.queue.insert(0, node)

    def pop(self):
        if not self.queue:
            raise
        return self.queue.pop()


class Solution:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, node):
        self.stack_in.append(node)

    def pop(self):
        if not self.stack_out:  # if stack_out is empty we upload the new incoming element in stack_in
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

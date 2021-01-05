# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.flag = 0

    def judge(self, root_val, right_tree):
        if right_tree:
            for element in right_tree:
                if element < root_val:
                    return 1
        return 0

    def spilt_and_judge(self, sequence):
        root_val = sequence[-1]
        boundary = 0
        while root_val > sequence[boundary]:
            boundary += 1
        left_sequence = sequence[:boundary]
        right_sequence = sequence[boundary:-1]
        return left_sequence, right_sequence, self.judge(root_val, right_sequence)

    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return
        left_sequence, right_sequence, judge = self.spilt_and_judge(sequence)
        self.flag += judge
        self.VerifySquenceOfBST(left_sequence)
        self.VerifySquenceOfBST(right_sequence)
        return True if not self.flag else False


if __name__ == '__main__':
    post = [4, 8, 6, 12, 16, 14, 10]
    post1 = [4, 6, 8, 12, 16, 14, 10]
    post2 = [4, 10, 6, 12, 16, 14, 8]
    post3 = [7, 4, 9, 3, 8, 11, 12, 10]
    solution = Solution()
    print(solution.VerifySquenceOfBST(sequence=post3))

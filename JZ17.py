class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def __init__(self):
        self.nodes = []
        self.temp1_pre, self.temp1_mid = [], []
        self.val2_pre, self.val2_mid = [], []

    def _pre_order_traversal(self, root, choice):
        if root is not None:
            if choice == '0':
                self.nodes.append(root)
            elif choice == '1':
                self.temp1_pre.append(root.val)
            else:
                self.val2_pre.append(root.val)
            self._pre_order_traversal(root.left, choice)
            self._pre_order_traversal(root.right, choice)
            return

    def _mid_order_traversal(self, root, choice):
        if root is not None:
            self._mid_order_traversal(root.left, choice)
            if choice == '0':
                self.nodes.append(root)
            elif choice == '1':
                self.temp1_mid.append(root.val)
            else:
                self.val2_mid.append(root.val)
            self._mid_order_traversal(root.right, choice)
            return

    @staticmethod
    def is_sub_list(lst1, lst2):
        if len(lst1) < len(lst2):
            return False
        return lst1[:len(lst2)] == lst2

    def check(self, node):
        self._pre_order_traversal(node, '1')
        self._mid_order_traversal(node, '1')
        return self.is_sub_list(self.temp1_pre, self.val2_pre) and self.is_sub_list(self.temp1_mid, self.val2_mid)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if (not pRoot1) or (not pRoot2):
            return False
        self._pre_order_traversal(pRoot1, '0')
        self._pre_order_traversal(pRoot2, '2')
        for node in self.nodes:
            self.temp1_pre, self.temp1_mid = [], []
            if self.check(node):
                return True
        return False


if __name__ == '__main__':
    # case 2
    pRoot1 = TreeNode(8)
    pRoot1.left, pRoot1.right = TreeNode(8), TreeNode(7)
    pRoot1.left.left, pRoot1.left.right = TreeNode(9), TreeNode(3)
    pRoot1.left.right.left, pRoot1.left.right.right = TreeNode(4), TreeNode(7)

    pRoot2 = TreeNode(8)
    pRoot2.left, pRoot2.right = TreeNode(9), TreeNode(2)

    # case 1
    # pRoot1 = TreeNode(8)
    # pRoot1.left = TreeNode(8)
    # pRoot1.left.left = TreeNode(9)
    # pRoot1.left.left.left = TreeNode(2)
    # pRoot1.left.left.left.left = TreeNode(5)
    #
    # pRoot2 = TreeNode(8)
    # pRoot2.left = TreeNode(9)
    # pRoot2.left.left = TreeNode(2)

    solution = Solution()
    print(solution.HasSubtree(pRoot1, pRoot2))

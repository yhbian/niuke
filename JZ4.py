def _pre_order_traversal(root):
    if root is not None:
        print(root.val)
        _pre_order_traversal(root.left)
        _pre_order_traversal(root.right)
    return


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def __init__(self):
        self.root = None

    def split(self, pre, tin):
        this_root = pre[0]
        idx = tin.index(this_root)
        left_tin, right_tin = tin[:idx], tin[idx+1:]
        left_pre, right_pre = pre[1: 1+idx], pre[1+idx:]
        return left_pre, right_pre, left_tin, right_tin

    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        if pre:
            root = TreeNode(pre[0])
            left_pre, right_pre, left_tin, right_tin = self.split(pre, tin)
            root.left = self.reConstructBinaryTree(left_pre, left_tin)
            root.right = self.reConstructBinaryTree(right_pre, right_tin)
            return root


if __name__ == '__main__':
    # define Tree
    pre, tin = [1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7]
    solution = Solution()
    root = solution.reConstructBinaryTree(pre, tin)
    _pre_order_traversal(root)

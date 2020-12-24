class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def _mid_order_traversal(self, root):
        if root is not None:
            self._mid_order_traversal(root=root.left)
            self.mid_order_nodes.append(root)
            self._mid_order_traversal(root=root.right)
            return
        return

    def KthNode(self, pRoot, k):
        # write code here
        self.mid_order_nodes = []
        self._mid_order_traversal(root=pRoot)
        if not k or k > len(self.mid_order_nodes):
            return None
        return self.mid_order_nodes[k-1]


if __name__ == '__main__':
    # define Tree
    leaf1 = TreeNode(2)
    leaf2 = TreeNode(4)
    leaf3 = TreeNode(6)
    leaf4 = TreeNode(8)
    left_branch = TreeNode(3)
    left_branch.left = leaf1
    left_branch.right = leaf2
    right_branch = TreeNode(7)
    right_branch.left = leaf3
    right_branch.right = leaf4
    root = TreeNode(5)
    root.left = left_branch
    root.right = right_branch

    # test
    print(Solution().KthNode(pRoot=root, k=8).val)
    # Solution()._mid_order_traversal(root=root)

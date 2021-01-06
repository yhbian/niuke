class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.nodes = []

    def mid_order_traversal(self, root):
        if root is not None:
            self.mid_order_traversal(root.left)
            self.nodes.append(root)
            self.mid_order_traversal(root.right)

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        self.mid_order_traversal(pRootOfTree)
        if len(self.nodes) == 1:
            return self.nodes[0]
        for idx in range(len(self.nodes)-1):
            self.nodes[idx].right = self.nodes[idx+1]
        self.nodes[-1].right = None
        for idx in range(len(self.nodes)-1, 0, -1):
            self.nodes[idx].left = self.nodes[idx-1]
        self.nodes[0].left = None
        return self.nodes[0]


if __name__ == '__main__':
   root = TreeNode(4)
   root.left, root.right = TreeNode(2), TreeNode(6)
   root.left.left, root.left.right = TreeNode(1), TreeNode(3)
   root.right.left, root.right.right = TreeNode(5), TreeNode(7)
   solution = Solution()
   head = solution.Convert(root)


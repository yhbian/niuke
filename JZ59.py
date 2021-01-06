class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.vals = []

    def _to_matrix(self, node_list):
        vals = []
        for node in node_list:
            vals.append(node.val)
        return vals

    def _bfs(self, root):
        node_list = [root]
        self.vals.append([root.val])
        while node_list:
            new_list = []
            for node in node_list:
                if node.left is not None:
                    new_list.append(node.left)
                if node.right is not None:
                    new_list.append(node.right)
            node_list = new_list
            if node_list:
                self.vals.append(self._to_matrix(node_list))

    @staticmethod
    def _inverse(lst):
        new_lst = []
        while lst:
            new_lst.append(lst.pop())
        return new_lst

    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        self._bfs(pRoot)
        for idx in range(len(self.vals)):
            if idx % 2:
                self.vals[idx] = self._inverse(self.vals[idx])
        return self.vals


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    root.left, root.right = TreeNode(2), TreeNode(6)
    root.left.left, root.left.right = TreeNode(1), TreeNode(3)
    root.right.left, root.right.right = TreeNode(5), TreeNode(7)
    solution.Print(root)

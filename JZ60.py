class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        lst = []
        if not pRoot:
            return lst
        node_list = [pRoot]
        while len(node_list):
            new_list = []
            val_list = []
            for node in node_list:
                val_list.append(node.val)
                if node.left is not None:
                    new_list.append(node.left)
                if node.right is not None:
                    new_list.append(node.right)
            lst.append(val_list)
            node_list = new_list
        return lst


if __name__ == '__main__':
    # define Tree
    leaf1 = TreeNode(5)
    leaf2 = TreeNode(7)
    leaf3 = TreeNode(9)
    leaf4 = TreeNode(11)
    left_branch = TreeNode(6)
    left_branch.left = leaf1
    left_branch.right = leaf2
    right_branch = TreeNode(10)
    right_branch.left = leaf3
    right_branch.right = leaf4
    root = TreeNode(8)
    root.left = left_branch
    root.right = right_branch

    # test code
    solution = Solution()
    matrix = solution.Print(pRoot=root)
    print(matrix)

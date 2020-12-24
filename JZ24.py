import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sum(self, path):
        sum = 0
        val_path = []
        for node in path:
            val_path.append(node.val)
            sum += node.val
        return sum, val_path

    def FindPath(self, root, expectNumber):
        if not root:
            return []
        candicate = {}  # {sum: [list1, list2]}, list1 = [root, node1, node2, ..., leaf]
        path_list = [[root]]
        while len(path_list):
            new_list = []
            for path in path_list:
                node = path[-1]
                path1, path2 = copy.copy(path), copy.copy(path)
                if node.right is not None:
                    path1.append(node.right)
                    new_list.append(path1)
                if node.left is not None:
                    path2.append(node.left)
                    new_list.append(path2)
                if (node.right is None) and (node.left is None):  # end of a path
                    sum, val_path = self.sum(path=path)
                    if sum not in candicate:
                        candicate[sum] = [val_path]
                    else:
                        candicate[sum].append(val_path)
            path_list = new_list
        if expectNumber in candicate.keys():
            return sorted(candicate[expectNumber])
        else:
            return []


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
    print(Solution().FindPath(root, expectNumber=29))

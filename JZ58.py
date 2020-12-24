class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirror(self, root):
        t = root.left
        root.left = root.right
        root.right = t
        if root.left is not None:
            self.mirror(root.left)
        if root.right is not None:
            self.mirror(root.right)
        return root

    def judge(self, lst):
        for i in lst:
            if i is not None:
                return 1
        return 0

    def skip(self, i):
        s = ''
        for k in range(i):
            s += '#' + '!'
        return s

    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        node_list = [root]
        s = str(root.val) + '/'
        i = 1
        while self.judge(node_list):
            new_list = []
            for node in node_list:
                if node is not None:
                    if node.left is not None:
                        new_list.append(node.left)
                        s += str(node.left.val) + '!'
                    else:
                        new_list.append(None)
                        s += '#' + '!'
                    if node.right is not None:
                        new_list.append(node.right)
                        s += str(node.right.val) + '!'
                    else:
                        new_list.append(None)
                        s += '#' + '!'
                else:
                    new_list.append(None)
                    s += self.skip(i)
            node_list = new_list
            s += '/' + '!'
            i += 1
        return s

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        s1 = self.Serialize(root=pRoot)
        s2 = self.Serialize(root=self.mirror(root=pRoot))
        return s1 == s2


if __name__ == '__main__':
    # case 1
    # root = TreeNode(x=8)
    # root.left = TreeNode(x=6)
    # root.right = TreeNode(x=6)
    # root.left.left = TreeNode(x=5)
    # root.left.right = TreeNode(x=7)
    # root.right.left = TreeNode(x=7)
    # root.right.right = TreeNode(x=5)

    # case 2
    root = TreeNode(x=5)
    root.left = TreeNode(x=5)
    root.right = TreeNode(x=5)
    root.left.left = TreeNode(x=5)
    root.left.right = None
    root.right.left = None
    root.right.right = TreeNode(x=5)
    root.left.left.left = TreeNode(x=5)
    root.left.left.right = None
    root.right.right.left = TreeNode(x=5)
    print(Solution().isSymmetrical(pRoot=root))



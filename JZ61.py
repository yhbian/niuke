import Tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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

    def Deserialize(self, s):
        # write code here
        if s == '#':
            return None
        s = s.split('/')[:-2]
        if len(s) == 1:
            return TreeNode(x=int(s[0]))
        root = TreeNode(x=int(s[0]))
        nodes = [root]
        for layer in range(1, len(s)):
            s_layer = [t for t in s[layer].split('!') if t is not '']
            layer_nodes = []
            i = 0
            for node in nodes:
                if s_layer[i] is not '#':
                    node.left = TreeNode(x=int(s_layer[i]))
                    layer_nodes.append(node.left)
                else:
                    layer_nodes.append(None)
                i += 1
                if s_layer[i] is not '#':
                    node.right = TreeNode(x=int(s_layer[i]))
                    layer_nodes.append(node.right)
                else:
                    layer_nodes.append(None)
                i += 1
            nodes = layer_nodes
        return root


if __name__ == '__main__':
    # # sample 1
    root = TreeNode(x=5)
    root.right = TreeNode(x=4)
    root.right.right = TreeNode(x=3)
    root.right.right.right = TreeNode(x=2)
    #
    # # sample 2
    # Tree = {5,#,4,#,3,#,2}

    # sample 3
    # root = TreeNode(x=8)
    # root.left = TreeNode(x=6)
    # root.right = TreeNode(x=10)
    # root.left.left = TreeNode(x=7)
    # root.left.right = TreeNode(x=9)
    # root.right.left = TreeNode(x=11)
    # root.right.right = TreeNode(x=13)

    # test
    solution = Solution()
    s = solution.Serialize(root=root)
    print(s)
    recovered = solution.Deserialize(s=s)
    Tree._pre_order_traversal(root=recovered)

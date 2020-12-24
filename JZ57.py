class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  # to parent


class Solution:
    def mid_order_traversal(self, root):
        if root is not None:
            self.mid_order_traversal(root.left)
            self.mid_list.append(root)
            self.mid_order_traversal(root.right)
            return
        return

    def GetNext(self, pNode):
        # write code here
        # get root
        root = pNode
        while root.next is not None:
            root = root.next
        self.mid_list = []
        self.mid_order_traversal(root=root)
        for i in range(len(self.mid_list)):
            if self.mid_list[i] == pNode:
                if i == len(self.mid_list) - 1:
                    return None
                else:
                    return self.mid_list[i+1]


if __name__ == '__main__':
    # # sample 1
    # root = TreeNode(x=5)
    # root.right = TreeNode(x=4)
    # root.right.right = TreeNode(x=3)
    # root.right.right.right = TreeNode(x=2)

    # sample 2
    root = TreeLinkNode(x=8)
    root.left = TreeLinkNode(x=6)
    root.left.next = root
    root.right = TreeLinkNode(x=10)
    root.right.next = root
    root.left.left = TreeLinkNode(x=5)
    root.left.left.next = root.left
    root.left.right = TreeLinkNode(x=7)
    root.left.right.next = root.left
    root.right.left = TreeLinkNode(x=9)
    root.right.left.next = root.right
    root.right.right = TreeLinkNode(x=11)
    root.right.right.next = root.right

    # test
    solution = Solution()
    next_node = solution.GetNext(pNode=root.left.left)
    print(next_node.val)

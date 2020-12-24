class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def link2list(self, pHead):
        lst = []
        while pHead is not None:
            lst.append(pHead.val)
            pHead = pHead.next
        return lst

    def list2link(self, lst):
        if not lst:
            return None
        if len(lst) == 1:
            return ListNode(lst[0])

        node, next_node = None, ListNode(lst[-1])
        for i in range(1, len(lst)):
            # construct the LinkList from tail to head
            node = ListNode(lst[-i-1])
            node.next = next_node
            next_node = node
        return node

    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return pHead
        repeats = {}
        pHead_ = pHead
        while pHead_ is not None:
            val = pHead_.val
            if val not in repeats.keys():
                repeats[val] = 1
            else:
                repeats[val] += 1
            pHead_ = pHead_.next

        lst = self.link2list(pHead=pHead)
        new_lst = []
        for val in lst:
            if repeats[val] < 2:
                new_lst.append(val)
        return self.list2link(lst=new_lst)




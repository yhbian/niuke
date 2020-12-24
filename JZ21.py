# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        assist = [pushV[0]]
        i = 1
        for to_pop in popV:
            if len(assist) == 0:
                assist.append(pushV[i])
                i += 1
            while (i < len(pushV)) and (assist[-1] != to_pop):
                assist.append(pushV[i])
                i += 1
            if assist[-1] == to_pop:
                assist.pop()
                continue

        if not len(assist):
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().IsPopOrder(pushV=[1,2,3,4,5], popV=[4,3,5,1,2]))
# Note: Learn to simulate the work manner of stack is a method.

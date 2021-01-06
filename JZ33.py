import copy

class Solution_slow:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # TODO:
        n = 1
        if index == 1:
            return n
        while index-1:
            n += 1
            k = copy.copy(n)
            while 1:
                if not k % 2:
                    k = k/2
                if not k % 3:
                    k = k/3
                if not k % 5:
                    k = k/5
                if (k % 2) * (k % 3) * (k % 5):
                    if k == 1:
                        index -= 1
                    break
        return n


class Solution:
    def next_number(self, dp):
        candidate = []
        for element in dp:
            if element * 2 > dp[-1]:
                candidate.append(element * 2)
            if element * 3 > dp[-1]:
                candidate.append(element * 3)
            if element * 5 > dp[-1]:
                candidate.append(element * 5)
        return min(candidate)

    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        dp = [1, 2, 3, 4, 5, 6]
        if index <= 6:
            return dp[index-1]
        while len(dp) < index:
            dp.append(self.next_number(dp))
        return dp[-1]


if __name__ == '__main__':
    solution1 = Solution_slow()
    solution2 = Solution()
    print(solution2.GetUglyNumber_Solution(7))

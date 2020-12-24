# -*- coding:utf-8 -*-
class Solution:
    def location_score(self, n1, n2):
        score = 0
        for num in list(str(n1)):
            score += int(num)
        for num in list(str(n2)):
            score += int(num)
        return score

    def movingCount(self, threshold, rows, cols):
        # write code here
        counts = 0

        if rows == 1:
            while self.location_score(0, counts) <= threshold and counts < cols:
                  counts += 1
            return counts

        if cols == 1:
            while self.location_score(counts, 0) <= threshold and counts < rows:
                  counts += 1
            return counts

        for i in range(rows):
            for j in range(cols):
                counts += self.location_score(i, j) <= threshold
        return counts


if __name__ == '__main__':
    solution = Solution()
    counts = solution.movingCount(threshold=10, rows=100, cols=1)
    print(counts)

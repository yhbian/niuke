# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    @staticmethod
    def rotate(matrix):
        m, n = len(matrix), len(matrix[0])
        rotated = [[None for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                rotated[n-i-1][j] = matrix[j][i]
        return rotated

    def printMatrix(self, matrix):
        # write code here
        lst = []
        if not matrix:
            return lst
        while matrix:
            lst.extend(matrix.pop(0))
            if not matrix:
                return lst
            matrix = self.rotate(matrix)


if __name__ == '__main__':
    matrix = [[1, 2], [3, 4]]
    solution = Solution()
    print(solution.printMatrix(matrix))

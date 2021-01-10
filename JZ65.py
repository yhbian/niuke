# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.flag = 0
        self.trace = []
        self.start_index = []

    def hasPath(self, matrix, rows, cols, path, step=0, start=None):
        # write code here
        if self.flag > 0:
            return

        # special case
        if not path:
            return False

        if rows == 1 and cols == 1:
            return matrix == path

        # for first step, we location starting index list, fire the recursion process
        if not step:
            first_str = path[0]
            for i, element in enumerate(matrix):
                if element == first_str:
                    self.start_index.append(i)
            for start in self.start_index:
                self.trace = [start]  # init the trace
                self.hasPath(matrix, rows, cols, path, step=1, start=start)

        # for succeeding steps
        anchor = start
        for candidate in [anchor - 1, anchor + 1, anchor - cols, anchor + cols]:
            if 0 <= candidate < rows * cols and candidate not in self.trace:
                if matrix[candidate] == path[step]:  # matched
                    self.trace.append(candidate)
                    if step == len(path) - 1:
                        self.flag += 1
                    else:
                        self.hasPath(matrix, rows, cols, path, step=step+1, start=candidate)

        return self.flag > 0


if __name__ == '__main__':
    matrix, rows, cols, path = "ABCESFCSADEE", 3, 4, "ABCCED"
    # matrix, rows, cols, path = "ABCESFCSADEE", 3, 4, "ABCB"
    # matrix, rows, cols, path = "A", 1, 1, "A"
    solution = Solution()
    print(solution.hasPath(matrix, rows, cols, path))

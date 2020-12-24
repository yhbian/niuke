class Solution:
    def minPathSum(self , matrix ):
        # write code here
        dp = matrix.copy()  # to store the sum
        first_row_sum = 0
        for i in range(len(matrix)):  # i = down steps
            for j in range(len(matrix[0])):  # j = right steps, i <= j
                if i == 0:  # first row
                    if j == 0:
                        dp[i][j] = matrix[0][0]
                        first_row_sum += matrix[0][0]
                    else:
                        first_row_sum += matrix[i][j]
                        dp[i][j] = first_row_sum
                elif j == 0 :  # diag
                    dp[i][j] = dp[i-1][j] + matrix[i][j]
                else: # ordinary elements
                    if dp[i-1][j] > dp[i][j-1]:
                        dp[i][j] = dp[i][j-1] + matrix[i][j]
                    else:
                        dp[i][j] = dp[i-1][j] + matrix[i][j]
        return dp[len(matrix)-1][len(matrix[0])-1]


if __name__ == '__main__':
    matrix = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
    solution = Solution()
    print(solution.minPathSum(matrix))

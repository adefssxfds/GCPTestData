class Solution(object):
    def minDistance(self, word1, word2):

        m , n = len(word1), len(word2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for index_i in range(m+1):
            for index_j in range(n+1):
                if index_i == 0:
                    dp[index_i][index_j] = index_j
                elif index_j == 0:
                    dp[index_i][index_j] = index_i
                elif word1[index_i-1] == word2[index_j-1]:
                    dp[index_i][index_j] = dp[index_i-1][index_j-1]
                else:
                    dp[index_i][index_j] = 1 + min(dp[index_i-1][index_j], 
                                                   dp[index_i-1][index_j-1], 
                                                   dp[index_i][index_j-1])

        return dp[m][n]
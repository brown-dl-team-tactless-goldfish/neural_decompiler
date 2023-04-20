class Solution:
    def stoneGameVII(self, s: List[int]) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        p_sum = [0] + list(accumulate(s))
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                dp[i][j] = max(p_sum[j + 1] - p_sum[i + 1] - dp[i + 1][j], 
                               p_sum[j] - p_sum[i] - dp[i][j - 1]);
        return dp[0][len(s) - 1]
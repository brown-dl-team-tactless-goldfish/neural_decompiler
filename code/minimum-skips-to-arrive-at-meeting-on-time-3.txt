class Solution {
public:
   int minSkips(vector<int>& A, int s, int target) {
        int n = A.size();
        vector<int> dp(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            for (int j = n; j >= 0; --j) {
                dp[j] += A[i];
                if (i < n - 1)
                    dp[j] = (dp[j] + s - 1) / s * s;
                if (j > 0)
                    dp[j] = min(dp[j], dp[j - 1] + A[i]);
            }
        }
        for (int i = 0; i < n; ++i) {
            if (dp[i] <= (long)s * target)
                return i;
        }
        return -1;
    }
};
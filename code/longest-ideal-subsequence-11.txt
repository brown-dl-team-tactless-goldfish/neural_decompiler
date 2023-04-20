class Solution {
    public:
        int longestIdealString(string s, int k) {
            int dp[26] = {};
            int max_count = 0;
            for (char & c: s) {
                int i = c - 'a';
                int min_index = max(i - k, 0);
                int max_index = min(i + k, 25);
                for (int j = min_index; j <= max_index; ++j) {
                    dp[i] = max(dp[i], dp[j]);
                }
                max_count = max(max_count, ++dp[i]);
            }
            return max_count;
        }
};
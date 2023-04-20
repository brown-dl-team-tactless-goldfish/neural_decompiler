class Solution {
public:
    int mod = 1000000007;
    int dp[10001][7][7];

    int find(int index, int prev1, int prev2, int n) {
        if (index == n) {
            return 1;
        }
        
        if (dp[index][prev1][prev2] != -1) {
            return dp[index][prev1][prev2];
        }
        
        int ans = 0;
        for (int i = 1; i <= 6; i++) {
            if (i != prev1 && i != prev2 && (prev1 == 0 || __gcd(i, prev1) == 1)) {
                ans = (ans + find(index + 1, i, prev1, n)) % mod;
            }
        }
        
        return dp[index][prev1][prev2] = ans;
    }
    
    int distinctSequences(int n) {
        memset(dp, -1, sizeof(dp));
        return find(0, 0, 0, n);
    }
};
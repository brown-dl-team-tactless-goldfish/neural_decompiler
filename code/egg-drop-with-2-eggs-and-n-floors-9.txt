class Solution {
public:
    int twoEggDrop(int n) {
        int dp[3][n+1];
        for(int i = 0; i <= n; i++) dp[0][i] = INT_MAX;
        for(int i = 0; i <= n; i++) dp[1][i] = i;
        for(int i = 0; i <= 2; i++) dp[i][0] = 0;
        for(int i = 0; i <= 2; i++) dp[i][1] = 1;
    
            for(int j = 2; j <= n; j++){
                int curr_ans = INT_MAX;
                int l = 0, r = j-1;
                while(l < j && r >= 0){
                    curr_ans = min(curr_ans, max(dp[1][l], dp[2][r]));
                    l++; r--;
                }
              dp[2][j] = curr_ans+1;
            }
        return dp[2][n];
    }
};
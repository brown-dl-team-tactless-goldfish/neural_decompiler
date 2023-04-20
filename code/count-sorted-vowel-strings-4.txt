class Solution {
public:
    int countVowelStrings(int n) {
        int dp[55];
        dp[1] = 5;
        dp[2]=15;
        for(int i = 3;i<=n;i++){
            dp[i] =(dp[i-1] * (4+i))/i;
        }
        return dp[n];
    }
};
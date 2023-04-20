class Solution {
public:
    
    int numSquares(int n) {
        if (n < 4){
            return n;
        }
        vector <int> dp(n + 1, INT_MAX);
        for (int index = 0; index < 4; index ++ ){
            dp[index] = index;
        }
        dp[4] = 1;
        
        for (int index = 5; index <= n; index ++ ){
            for (int curr = 2; curr < index; curr ++ ){
                if (curr * curr > index){
                    break;
                }
            dp[index] = min(dp[index], 1 + dp[index - curr * curr]);    
            }
        }
        return dp[n];
    }
};
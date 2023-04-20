class Solution {
public:
    int superEggDrop(int k, int n) {
        int dp[k+1][n+1];
        for(int i = 0; i <= n; i++) dp[0][i] = INT_MAX;
        for(int i = 0; i <= n; i++) dp[1][i] = i;
        for(int i = 0; i <= k; i++) dp[i][0] = 0;
        for(int i = 0; i <= k; i++) dp[i][1] = 1;
        
        for(int i = 2; i <= k; i++)
            for(int j = 2; j <= n; j++) {
               int l = 1, r = j, temp = 0, ans = INT_MAX;
                 while(l <= r) {
                    int mid = (l + r)/2;
                    int left = dp[i-1][mid-1]; 
                    int right = dp[i][j-mid];  
                    temp = 1 + max(left,right);         
                    if(left < right) l = mid+1;                       
                    else r = mid-1;
                    ans = min(ans,temp);               
                 }
                 dp[i][j]=ans;
            }
        return dp[k][n];
    }
};
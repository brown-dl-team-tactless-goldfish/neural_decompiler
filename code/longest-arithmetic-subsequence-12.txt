class Solution {
public:
    int longestArithSeqLength(vector<int>& A) {
        
        int n = A.size();
        if(n==2)return n;
        
        
        return LAIS(A);
    }
    
    int LAIS(vector<int>&A)
    {
        int TAG = 500;
        vector<vector<int>>dp(A.size(),vector<int>(2*(TAG+1),1));
        int maxL = 1;
        int n = A.size();
        int diff;
        for(int i= 1;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                diff = A[i]-A[j] + TAG;
                dp[i][diff] = max(dp[i][diff],dp[j][diff] + 1);
                maxL = max(maxL,dp[i][diff]);
            }
        }
        
        return maxL;
    }
};
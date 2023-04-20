class Solution {
public:
    int fun(int start,int end,vector<vector<int>> &dp)
    {
        if(start>=end)
        return 0;
        if(dp[start][end]!=-1)
        return dp[start][end];
        int ans=INT_MAX;
        for(int i=start;i<=end;i++)
        {
            ans=min(ans,i+max(fun(start,i-1,dp),fun(i+1,end,dp)));
        }
        return dp[start][end]=ans;
    }
    int getMoneyAmount(int n) {
      vector<vector<int>> dp(n+1,vector<int>(n+1,-1));
      return fun(1,n,dp);  
    }
};
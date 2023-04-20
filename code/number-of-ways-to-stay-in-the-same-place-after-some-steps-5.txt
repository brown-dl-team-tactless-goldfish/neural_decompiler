class Solution {
public:
    int dp[501][501];
    int M=1e9+7;
    int solve(int pos, int n, int steps){
        if(steps==0){
            if(pos==0)
                return 1;
            return 0;
        }
        if(dp[pos][steps]!=-1)
            return dp[pos][steps];
        int ans=0;
        if(pos-1>=0)
            ans=(ans%M+solve(pos-1,n,steps-1)%M)%M;
        if(pos+1<n)
            ans=(ans%M+solve(pos+1,n,steps-1)%M)%M;
        ans=(ans%M+solve(pos,n,steps-1)%M)%M;
        return dp[pos][steps]=ans;
    }
    int numWays(int steps, int n) {
        memset(dp,-1,sizeof(dp));
        if(steps<=n)
            n=steps;
        return solve(0,n,steps);
    }
};
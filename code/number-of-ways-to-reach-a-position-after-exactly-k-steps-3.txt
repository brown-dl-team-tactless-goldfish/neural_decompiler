class Solution {
public:

    // dp and mod
    const int mod = 1e9 + 7;
    long dp[3100][1001];
    
    long helper(int start , int end , int k){
        if(start==end){
           if(k==0) return 1;
        }
        if(k==0) return 0;

        // dp
        if(dp[start+1000][k]!=-1) return dp[start+1000][k];


        long ans = helper(start+1,end,k-1);

        // if steps are sufficient to get back
        if((k-1) >= (end-start+1)){
            ans += helper(start-1,end,k-1);
        }
        return dp[start+1000][k]=ans%mod;
    }
    int numberOfWays(int sp, int ep, int k) {
        memset(dp,-1,sizeof(dp));
        if(abs(sp-ep)>k) return 0;
        
        // helper
        long ans = helper(sp,ep,k);
        return ans%mod;
    }
};
class Solution {
public:
    int dp[5002][7][16];
    vector<int> roll;
    int mod=1e9+7;
    
    int dfs(int n, int prev, int count){
        if(n==0) return 1;
        if(dp[n][prev][count]!=-1) return dp[n][prev][count];
        
        long long int res=0;
        
        for(int i=0;i<6;i++){
            if(i==prev && count>=roll[i]) continue;
            if(i==prev){
                res = (res+dfs(n-1,prev,count+1))%mod;
            }
            else res = (res+dfs(n-1,i,1))%mod;
        }
        return dp[n][prev][count]=res;
    }
    
    int dieSimulator(int n, vector<int>& rollMax) {
        roll=rollMax;

        memset(dp,-1,sizeof dp);
        
        return dfs(n,6,0);
    }
};
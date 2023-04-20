class Solution {
public:
    int MOD = 1e9+7;
    int dp[5001][4][4][4];
    long long dfs(int i,int n,int a,int b,int c){
        if(i == n){
            return 1;
        }
        
        if(dp[i][a][b][c] != -1) return dp[i][a][b][c];
        long long t = 0;
        for(int j = 1; j < 4; j++){
            for(int k = 1; k < 4; k++){
                for(int l = 1; l < 4; l++){
                    if(j != a && k != b && l != c && j != k && k != l){
                        t = (t + dfs(i+1,n,j,k,l))%MOD;
                    }
                }
            }
        }
        
        dp[i][a][b][c] = t;
        return t;
        
    }
    
    int numOfWays(int n) {
        memset(dp,-1,sizeof(dp));
        return dfs(0,n,0,0,0);
    }
};
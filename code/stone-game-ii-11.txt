class Solution {
public:
    int N;
    vector<int> pre;
    int dp[111][511][2];
    int solve(int id, int m, int turn){
        if(id>=N+1){
            return 0;
        }
        if(dp[id][m][turn] != -1){
            return dp[id][m][turn];
        }
        int ans = (turn == 1)?INT_MAX: INT_MIN;
        for(int i=1;i<=2*m && (id+i-1)<=N;i++){
            if(turn == 1){
                ans = min(ans, solve(id+i,max(m,i),0));
            }else{
                ans = max(ans, pre[id+i-1]-pre[id-1] + solve(id+i,max(m,i),1));
            }
        }
        return dp[id][m][turn] = ans;
    }
    
    
    int stoneGameII(vector<int>& piles) {
        
        N = piles.size();
        memset(dp,-1,sizeof dp);
        pre.resize(N+2,0);
        for(int i=0;i<N;i++){
            pre[i+1] = pre[i] + piles[i];
        }
        return solve(1,1,0);
    }
};
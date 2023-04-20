class Solution {
public:
    int n,m;
    int mx = 1e4;
    
    int solve(vector<vector<int>>& grid, int k,int i,int j,vector<vector<int>>&vis,vector<vector<vector<int>>>&dp){
        // cout<<i<<" "<<j<<endl;
        int a = mx,b = mx,c = mx,d = mx;
     

        if(i>=n || j>=m || i<0 || j<0 || vis[i][j] == 0){
            return mx;
        }

        if(dp[i][j][k]!=-1){
            return dp[i][j][k];
        }

        if(i==0 and j==0){
            return dp[i][j][k] = 0;
        }


        if(grid[i][j]==1){
            if(k>0){
                k--;
            }
            else{
                return dp[i][j][k] = mx;
            }
        }

        vis[i][j] = 0;
        
        
        if(i-1>=0 ){
            c = solve(grid,k,i-1,j,vis,dp);
        }
        if(j-1>=0){
            d = solve(grid,k,i,j-1,vis,dp);
        }
        if(i+1<n){
            a = solve(grid,k,i+1,j,vis,dp);
        }
        if(j+1<m){
            b = solve(grid,k,i,j+1,vis,dp);
        }
        vis[i][j] = 1;
        
        return dp[i][j][k] = 1 + min({a,b,c,d});
    }
    int shortestPath(vector<vector<int>>& grid, int k) {
        n = grid.size();
        m = grid[0].size();
        vector<vector<int>>vis(n,vector<int>(m,1));
        vector<vector<vector<int>>>dp(n,vector<vector<int>>(m,vector<int>(k+1,-1)));
        int ans =  solve(grid,k,n-1,m-1,vis,dp);
        
        if(ans>=mx){
            return -1;
        }
        return ans;
    }
};
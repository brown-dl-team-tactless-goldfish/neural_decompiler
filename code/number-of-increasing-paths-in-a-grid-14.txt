class Solution {
public:
    int mod=1e9+7;
    int fun(vector<vector<int>>& grid,int i,int j,vector<vector<int>>& dp)
    {
        if(dp[i][j]!=0) return dp[i][j];
        
        int m=grid.size();
        int n=grid[0].size();
        
        if(i<0 && j<0 && i>=m && j>=n)
        {
            return 0;
        }
        
        int res=1;
        
        if(i>0 && grid[i][j]<grid[i-1][j])
        {
            res=res%mod+fun(grid,i-1,j,dp)%mod;
        }
        if(j>0 && grid[i][j]<grid[i][j-1])
        {
            res=res%mod+fun(grid,i,j-1,dp)%mod;
        }
        if(i<m-1 && grid[i][j]<grid[i+1][j])
        {
            res=res%mod+fun(grid,i+1,j,dp)%mod;
        }
        if(j<n-1 && grid[i][j]<grid[i][j+1])
        {
            res=res%mod+fun(grid,i,j+1,dp)%mod;
        }
        
        return dp[i][j]=res%mod;
    }
    
    int countPaths(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        
        vector<vector<int>> dp(m,vector<int>(n,0));
        
        int res=0;
        
        
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                res=(res%mod+ fun(grid,i,j,dp)%mod)%mod;
            }
        }
        
        return res;
    }
};
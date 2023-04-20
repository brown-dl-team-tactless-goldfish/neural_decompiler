class Solution {
    int n, m;
    bool dfs(int x, int y, int open, vector<vector<char>>& grid, vector<vector<vector<int>>> &dp)
    {
        if(x >= n || y >= m) return false;
        if(grid[x][y] == '(')
            open++;
        else
            open--;
        if(open < 0)
            return false;
        if(dp[x][y][open] != -1)
            return dp[x][y][open];
        if(x == n-1 && y == m-1)
        {
            if(open == 0)
                return true;
            return false;
        }
        bool val = dfs(x+1, y, open, grid, dp) || dfs(x, y+1, open, grid, dp);
        return dp[x][y][open] = val;
    }
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        n = grid.size(), m = grid[0].size();
        vector<vector<vector<int>>> dp(n+1, vector<vector<int>> (m+1, vector<int> (201, -1)));
        return dfs(0,0,0,grid,dp);
    }
};
int dp[70][70][70];
int dfs(int ** grid, int size, int colSize, int i, int l, int r) {
    if(i >= size || l == r) return 0;
    if(l < 0 || l >= colSize || r < 0 || r >= colSize) return 0;
    if(dp[i][l][r] >= 0) return dp[i][l][r];
    int res = 0;
    int d[3] = {-1, 0, 1};
    for(int x = 0; x < 3; x++) 
        for(int y = 0; y < 3; y++) 
        {
            int temp = dfs(grid, size, colSize, i + 1, l + d[x], r + d[y]);
            res = res > grid[i][l] + grid[i][r] + temp ? res : grid[i][l] + grid[i][r] + temp;
        }
    return (dp[i][l][r] = res);
}
int cherryPickup(int** grid, int gridSize, int* gridColSize){
    memset(dp, -1, sizeof(dp));
    return dfs(grid, gridSize, *gridColSize, 0, 0, *gridColSize - 1);
}
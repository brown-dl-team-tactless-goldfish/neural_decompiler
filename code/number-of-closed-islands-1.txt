void dfs(int** grid, int r, int c, int rSize, int cSize, int** cache, int num) {
    if(r > rSize-1 || c > cSize-1 || r < 0 || c < 0 || cache[r][c] == 1 || grid[r][c] == 1) return;
    if(cache[r][c] == 0) cache[r][c] = 1;
    if(r == 0 || r == rSize-1 || c == 0 || c == cSize-1) {
        grid[r][c] = -1;
        dfs(grid, r-1, c, rSize, cSize, cache, num);
        dfs(grid, r+1, c, rSize, cSize, cache, num);
        dfs(grid, r, c-1, rSize, cSize, cache, num);
        dfs(grid, r, c+1, rSize, cSize, cache, num);
        return;
    }
    grid[r][c] = num;
    dfs(grid, r-1, c, rSize, cSize, cache, num);
    dfs(grid, r+1, c, rSize, cSize, cache, num);
    dfs(grid, r, c-1, rSize, cSize, cache, num);
    dfs(grid, r, c+1, rSize, cSize, cache, num);
}

int closedIsland(int** grid, int gridSize, int* gridColSize) {
    int rSize = gridSize, cSize = gridColSize[0];
    int** cache = (int**) malloc(rSize * sizeof(int*));
    for(int i = 0; i < rSize; i++) {
        cache[i] = calloc(cSize, sizeof(int));
    }
    
    int num = 1;
    for(int c = 0; c < cSize; c++) {
        if(grid[0][c] == 0) dfs(grid, 0, c, rSize, cSize, cache, num);
    }
    for(int c = 0; c < cSize; c++) {
        if(grid[rSize-1][c] == 0) dfs(grid, rSize-1, c, rSize, cSize, cache, num);
    }
    for(int r = 1; r < rSize-1; r++) {
        if(grid[r][0] == 0) dfs(grid, r, 0, rSize, cSize, cache, num);
    }
    for(int r = 1; r < rSize-1; r++) {
        if(grid[r][cSize-1] == 0) dfs(grid, r, cSize-1, rSize, cSize, cache, num);
    }
    for(int r = 1; r < rSize-1; r++) {
        for(int c = 1; c < cSize-1; c++) {
            if(grid[r][c] == 0) {
                num++;
                dfs(grid, r, c, rSize, cSize, cache, num);
            }
        }
    }
    
    for(int i = 0; i < rSize; i++) {
        free(cache[i]);
    }
    free(cache);
    return num-1;
}
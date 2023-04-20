#define MAX(a,b) a>b? a:b

int dfs(int** grid, int gridSize, int* gridColSize, int x, int y){
    if(x<0 || y<0 || x>=*gridColSize || y>= gridSize) return 0;
    if(grid[y][x]==0) return 0;

    grid[y][x] = 0;    

    return (1+dfs(grid, gridSize, gridColSize, x+1, y)
            +dfs(grid, gridSize, gridColSize, x-1, y)
            +dfs(grid, gridSize, gridColSize, x, y+1)
            +dfs(grid, gridSize, gridColSize, x, y-1));
}

 

int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize){
    int sum=0;
    int max = 0;   

    for(int i=0;i<gridSize;++i){
        for(int j=0;j<*gridColSize;++j){
            if(grid[i][j]==1){
                sum = dfs(grid, gridSize, gridColSize, j, i);
                max = MAX(sum, max);
            }
        }
    }
    return max;
}
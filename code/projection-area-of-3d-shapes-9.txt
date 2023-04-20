int max(int a,int b){
    return a>b?a:b;
}
int projectionArea(int** grid, int gridSize, int* gridColSize){
    int sum=0;
    // find x-y plane, y-z plane , x-z plane
    for(int row=0;row<gridSize;row++){
        int x_z_plane=0,y_z_plane=0;
        for(int col=0;col<*gridColSize;col++){
            x_z_plane=max(x_z_plane,grid[row][col]);
            y_z_plane=max(y_z_plane,grid[col][row]);
            if(grid[row][col]) ++sum; // x-y plane
        }
        sum+=(x_z_plane+y_z_plane);
    }
    return sum;
}
void DFS(int **grid, int ROW, int COL, int x, int y){
	if(x < 0 || y < 0 || x >= ROW || y >= COL) return;

	if(grid[x][y]!=1) return;

	//marked as visted
	grid[x][y] = 0;

	//DFS the neighbor
	DFS(grid, ROW, COL, x + 1, y);
	DFS(grid, ROW, COL, x - 1, y);
	DFS(grid, ROW, COL, x, y + 1);
	DFS(grid, ROW, COL, x, y - 1);
}


//remove the lands that in grid 2 but not in grid 1 (DFS), and DFS count for how many lands
int countSubIslands(int** grid1, int grid1Size, int* grid1ColSize, int** grid2, int grid2Size, int* grid2ColSize){
	for(int i = 0; i < grid2Size; i++){
		for(int j = 0; j < grid2ColSize[0]; j++){
			if(grid2[i][j]==1 && grid1[i][j]==0){
				DFS(grid2, grid2Size, grid2ColSize[0], i, j);
			}
		}
	}

	//count for the sublands
	int lands = 0;
	for(int i = 0; i < grid2Size; i++){
		for(int j = 0; j < grid2ColSize[0]; j++){
			if(grid2[i][j]==1){
				DFS(grid2, grid2Size, grid2ColSize[0], i, j);
				lands++;
			}
		}
	}
	return lands;
}
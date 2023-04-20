void DFS1(int **grid, int ROW, int COL, int x, int y){
	if(x < 0 || y < 0 || x >= ROW || y >= COL) return;

	//not the island
	if(grid[x][y]!=1) return;

	//mark as visted
	grid[x][y] = 2;

	//DFS the four neighbors
	DFS1(grid, ROW, COL, x + 1, y);
	DFS1(grid, ROW, COL, x - 1, y);
	DFS1(grid, ROW, COL, x, y + 1);
	DFS1(grid, ROW, COL, x, y - 1);	
}

void DFS2(int **grid, int ROW, int COL, int x, int y, int *lands){
	if(x < 0 || y < 0 || x >= ROW || y >= COL) return;

	//not the island and not marked
	if(grid[x][y]!=1) return;

	//mark as visted
	grid[x][y] = 0;
	(*lands)++;

	//DFS the four neighbors
	DFS2(grid, ROW, COL, x + 1, y, lands);
	DFS2(grid, ROW, COL, x - 1, y, lands);
	DFS2(grid, ROW, COL, x, y + 1, lands);
	DFS2(grid, ROW, COL, x, y - 1, lands);	
}

int numEnclaves(int** grid, int gridSize, int* gridColSize){

	//DFS the land near to the boundary and mark as 2
	for(int i = 0; i < gridSize; i++){
		for(int j = 0; j < gridColSize[0]; j++){
			if(i==0 || j==0 || i == gridSize - 1 || j == gridColSize[0] - 1){
				DFS1(grid, gridSize, gridColSize[0], i, j);
			}
		}
	}


	//DFS the remaining land in the grid
	int lands = 0;
	for(int i = 0; i < gridSize; i++){
		for(int j = 0; j < gridColSize[0]; j++){
			//ignore the marked lands and the sea
			if(grid[i][j]!=1) continue;
			DFS2(grid, gridSize, gridColSize[0], i, j, &lands);
		}
	}
	return lands;
}

//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////

void DFS(int **grid, int ROW, int COL, int x, int y, int *reduced_lands){
	if(x < 0 || y < 0 || x >= ROW || y >= COL) return;

	//not the island
	if(grid[x][y]!=1) return;

	//mark as visted
	grid[x][y] = 2;
	(*reduced_lands)++;

	//DFS the four neighbors
	DFS(grid, ROW, COL, x + 1, y, reduced_lands);
	DFS(grid, ROW, COL, x - 1, y, reduced_lands);
	DFS(grid, ROW, COL, x, y + 1, reduced_lands);
	DFS(grid, ROW, COL, x, y - 1, reduced_lands);	
}

//only DFS for once:
int numEnclaves(int** grid, int gridSize, int* gridColSize){

	//DFS the land near to the boundary and mark as 2
	int reduced_lands = 0;
	int sea_area_count = 0;
	for(int i = 0; i < gridSize; i++){
		for(int j = 0; j < gridColSize[0]; j++){
			if(grid[i][j]==0){
				sea_area_count++;
				continue;
			}
			if(i==0 || j==0 || i == gridSize - 1 || j == gridColSize[0] - 1){
				DFS(grid, gridSize, gridColSize[0], i, j, &reduced_lands);
			}
		}
	}
	return gridSize * gridColSize[0] - sea_area_count - reduced_lands;
}
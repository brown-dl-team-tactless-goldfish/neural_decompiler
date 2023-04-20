int islandPerimeter(int** grid, int gridSize, int* gridColSize){
    
    unsigned int perimeter = 0;
    
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            if (grid[i][j] == 0)
                continue;
            if (i == 0 && j == 0 && i == gridSize-1 && j == (*gridColSize)-1) {
                perimeter += 4;
                break;
            }
            if (i == 0)
                perimeter++;
            if (j == 0)
                perimeter++;
            if (i == gridSize-1)
                perimeter++;
            if (j == (*gridColSize)-1)
                perimeter++;
            if (i >0 && grid[i-1][j] == 0)
                perimeter++;
            if (i < gridSize-1 && grid[i+1][j] == 0)
                perimeter++;
            if (j > 0 && grid[i][j-1] == 0)
                perimeter++;
            if (j < (*gridColSize)-1 && grid[i][j+1] == 0)
                perimeter ++;
        }
    }
    return perimeter;
}
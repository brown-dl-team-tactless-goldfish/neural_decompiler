int min(int** list, int gridSize, int gridColSize, int now){
    int min = INT_MAX;
    for (int i = 0 ; i < now ; i++){
        if (min > list[gridSize][i]){
            min = list[gridSize][i];
        }
    }
    for (int i = now+1 ; i < gridColSize ; i++){
        if (min > list[gridSize][i]){
            min = list[gridSize][i];
        }
    }
    return min;
}

int minFallingPathSum(int** grid, int gridSize, int* gridColSize){
    int** list = malloc(sizeof(int*)*2);
    list[0] = malloc(sizeof(int)*(*gridColSize));
    list[1] = malloc(sizeof(int)*(*gridColSize));
    gridSize--;
    int k = gridSize % 2;
    for (int i = 0 ; i < *gridColSize ; i++){
        list[k][i] = grid[gridSize][i];
    }
    gridSize--;
    int other = k;
    while (gridSize >= 0){
        k = gridSize % 2;
        for (int i = 0 ; i < *gridColSize ; i++){
            list[k][i] = min(list, other, *gridColSize, i) + grid[gridSize][i];
        }
        other = k;
        gridSize--;
    }
    
    int ans = min(list, 0, *gridColSize, *gridColSize);
    free(list[0]);
    free(list[1]);
    free(list);
    return ans;
}
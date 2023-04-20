void getDistance(int ** mat, int ** result, int row, int col, int x, int y, int range)
{
    if(x < 0 || x >= row || y < 0 || y >= col) return;
    if((range == 0 || mat[x][y] == 1) && (result[x][y] == 0 || result[x][y] > range))
    {
        result[x][y] = range;
        getDistance(mat, result, row, col, x-1, y, range + 1);
        getDistance(mat, result, row, col, x+1, y, range + 1);
        getDistance(mat, result, row, col, x, y-1, range + 1);
        getDistance(mat, result, row, col, x, y+1, range + 1);
    }
}

int** updateMatrix(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes){
    int ** result = (int **)calloc(matSize*(*matColSize), sizeof(int *));
    *returnSize = matSize;
    *returnColumnSizes = (int *)malloc(matSize*sizeof(int));
    for(int i=0; i<matSize; i++)
    {
        (*returnColumnSizes)[i] = *matColSize;
        result[i] = (int *)calloc(*matColSize, sizeof(int));
    }
    for(int i=0; i<matSize; i++)
        for(int j=0; j<*matColSize; j++)
            if(mat[i][j] == 0)
                getDistance(mat, result, matSize, *matColSize, i, j, 0);
    return result;
}
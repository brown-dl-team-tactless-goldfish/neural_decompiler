

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes)
{
    int ** ret_arr = (int **)malloc(sizeof(int *) * gridSize);
    int ret_arr_index = 0;
    int i=0, j=0;
    for(i=0; i<gridSize; i++)
    {
        int * tmp_arr = (int *)malloc(sizeof(int) * (*gridColSize));
        ret_arr[ret_arr_index++] = tmp_arr;

    }
    
    int loop = 0;
    if(k == 0)
    {
        for(i=0; i<gridSize; i++)
        {
            for(j=0; j< *gridColSize; j++)
            {
                ret_arr[i][j] = grid[i][j];
            }
        }
    }
    
    
    for(loop=0; loop<k; loop++)
    {
        for(i=0; i<gridSize; i++)
        {
            for(j=0; j< *gridColSize; j++)
            {
                if(i != gridSize - 1 && j == *gridColSize - 1)
                {
                    ret_arr[i+1][0] = grid[i][j];
                }
                else if(i==gridSize - 1 && j == *gridColSize - 1)
                {
                    ret_arr[0][0] = grid[i][j];
                }
                else
                {
                    ret_arr[i][j+1] = grid[i][j];
                }
            }
        }
        
        for(i=0; i<gridSize; i++)
        {
            for(j=0; j< *gridColSize; j++)
            {
                grid[i][j] = ret_arr[i][j];
            }
        }
        
        
    }
    *returnSize = gridSize;
    
    int * ret_col = (int *)malloc(sizeof(int) * gridSize);
    for(i=0; i<gridSize; i++)
    {
        ret_col[i] = *gridColSize;
    }
    *returnColumnSizes = ret_col;
    return ret_arr;
}
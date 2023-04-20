

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes)
{
    if( r * c != matSize * (*matColSize))
    {  
        int ** ret_arr = (int **)malloc(sizeof(int *) * matSize);
        int ret_arr_index = 0;
        int i=0, j=0;
        for(i=0; i<matSize; i++)
        {
            int * tmp_arr = (int *)malloc(sizeof(int) * (*matColSize));
            int tmp_arr_index = 0;
            ret_arr[ret_arr_index++] = tmp_arr;
            
            for(j=0; j< *matColSize; j++)
            {
                tmp_arr[tmp_arr_index++] = mat[i][j];
            }
        }

        int * col_arr = (int *)malloc(sizeof(int) * matSize);
        for(i=0; i< matSize; i++)
        {
            col_arr[i] = *matColSize;
        }
        *returnColumnSizes = col_arr;
        *returnSize = matSize;
        return ret_arr;
    }
    else
    {
        int ** ret_arr = (int **)malloc(sizeof(int *) * r);
        int ret_arr_index = 0;
        int i=0, j=0;
        
        int col_rem_size = 0;
        int * tmp_col = NULL;
        int tmp_col_index = 0;
        
        if(col_rem_size == 0)
        {       
            tmp_col = (int *)malloc(sizeof(int) * c);        
            tmp_col_index = 0;
            ret_arr[ret_arr_index++] = tmp_col;
            col_rem_size = c;              
        }
        
        for(i=0; i<matSize; i++)
        {
                   
            for(j=0; j< *matColSize; j++)
            {
                tmp_col[tmp_col_index++] = mat[i][j];
                col_rem_size--;
                
                if(col_rem_size == 0)
                {    
                    if(ret_arr_index != r)
                    {
                        tmp_col = (int *)malloc(sizeof(int) * c);        
                        tmp_col_index = 0;
                        ret_arr[ret_arr_index++] = tmp_col;
                        col_rem_size = c;
                    }
                }
            }
        }
        
        int * col_arr = (int *)malloc(sizeof(int) * r);
        for(i=0; i< r; i++)
        {
            col_arr[i] = c;
        }
        *returnColumnSizes = col_arr;
        *returnSize = r;
        return ret_arr;
    }
    
    
    return NULL;
}
void merge(int arr[], int low, int mid, int high)
{
    int * ret_arr = (int *)malloc(sizeof(int) * (high-low+1));
    int ret_arr_index = 0;

    int i=0,j=0;
    for(i=low, j=mid+1; i<=mid && j<=high;)
    {
        if(arr[i] <= arr[j])
        {
            ret_arr[ret_arr_index++] = arr[i++];
        }
        else
        {
            ret_arr[ret_arr_index++] = arr[j++];
        }
    }

    while(i<=mid)
    {
        ret_arr[ret_arr_index++] = arr[i++];
    }

    while(j<=high)
    {
        ret_arr[ret_arr_index++] = arr[j++];
    }

    memcpy(&arr[low], ret_arr, sizeof(int)*(high-low+1));
    free(ret_arr);
}

void merge_sort(int arr[], int low, int high)
{
    if(low < high)
    {
        int mid = (low+high)/2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* luckyNumbers (int** matrix, int matrixSize, int* matrixColSize, int* returnSize)
{
    
    int rows = 0, columns = 0;
    
    int min_row_element = INT_MAX;
    int max_column_element = INT_MIN;
    
    int * min_arr = (int *)malloc(sizeof(int) * matrixSize);
    int min_arr_index = 0;
    int i=0,j=0;
    for(i=0; i<matrixSize; i++)
    {
        min_row_element = INT_MAX;
        for(j=0; j<*matrixColSize; j++ )
        {
            if(matrix[i][j] <= min_row_element)
            {
                min_row_element = matrix[i][j];
            }
        }
        min_arr[min_arr_index++] = min_row_element;
    }
    
    
    int * max_arr = (int *)malloc(sizeof(int) * (*matrixColSize));
    int max_arr_index = 0;
    
    for(j=0; j<*matrixColSize; j++)
    {
        max_column_element = INT_MIN;
        for(i=0; i<matrixSize; i++)
        {
            if(matrix[i][j] >= max_column_element)
            {
                max_column_element = matrix[i][j];
            }
        }
        max_arr[max_arr_index++] = max_column_element;
    }
    
    
    //Sort both the arrays
    merge_sort(min_arr, 0, min_arr_index-1);
    merge_sort(max_arr, 0, max_arr_index-1);
    
    int * merge_arr = (int *)malloc(sizeof(int) * (min_arr_index + max_arr_index));
    memcpy(&merge_arr[0], min_arr, sizeof(int)*min_arr_index);
    memcpy(&merge_arr[min_arr_index], max_arr, sizeof(int)*max_arr_index);
    merge_sort(merge_arr, 0, min_arr_index + max_arr_index-1);
    
    int * ret_arr = (int *)malloc(sizeof(int)  * (min_arr_index + max_arr_index));
    int ret_arr_index = 0;
    int prev_element = merge_arr[0];
    //Find the duplicates and assign in the array
    for(i=1; i<min_arr_index + max_arr_index; i++)
    {
        if(merge_arr[i] == prev_element)
        {
            ret_arr[ret_arr_index++] = merge_arr[i];
        }
        prev_element = merge_arr[i];
    }
    
    free(min_arr);
    free(max_arr);
    free(merge_arr);
    
    *returnSize = ret_arr_index;
    return ret_arr;
}
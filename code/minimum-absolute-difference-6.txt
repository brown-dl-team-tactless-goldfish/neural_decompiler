void merge(int arr[], int low, int mid, int high)
{
    int * ret_arr = (int *)malloc(sizeof(int) * (high - low + 1));
    int ret_arr_index = 0;
    
    int i=0,j=0;
    for(i=low, j=mid+1; i<=mid && j<=high; )
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
    
    memcpy(&arr[low], ret_arr, sizeof(int) * ret_arr_index);
    free(ret_arr);
}

void merge_sort(int arr[], int low, int high)
{
    if(low < high)
    {
        int mid = (low + high)/2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes)
{
    merge_sort(arr, 0, arrSize-1);
    
    int i=0;
    int min_diff = INT_MAX;
    
    for(i=1; i<arrSize; i++)
    {
        int diff = arr[i] - arr[i-1];
        if(diff < 0)
        {
            diff *= -1;
        }
        if(diff <= min_diff)
        {
            min_diff = diff;
        }
    }
    
    int ** ret_arr = (int **)malloc(sizeof(int *) * arrSize);
    int ret_arr_index = 0;
    
    int * column_arr = (int *)malloc(sizeof(int) * arrSize);
    int column_index = 0;
    
    for(i=1; i<arrSize; i++)
    {
        int diff = arr[i] - arr[i-1];
        if(diff < 0)
        {
            diff *= -1;
        }
        
        if(diff == min_diff)
        {
            int * new_arr = (int *)malloc(sizeof(int) * 2);
            new_arr[0] = arr[i-1];
            new_arr[1] = arr[i];
            ret_arr[ret_arr_index++] = new_arr;
            column_arr[column_index++] = 2;
        }
    }
    
    *returnColumnSizes = column_arr;
    *returnSize = ret_arr_index;
    return ret_arr;
}
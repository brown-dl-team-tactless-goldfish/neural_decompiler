void merge(int ** arr, int low, int mid, int high)
{
    int * new_arr = (int *)malloc(sizeof(int) * ((high-low+1)*2));
    int new_arr_index = 0;
    
    int i=0,j=0;
    for(i=low, j=mid+1; i<=mid && j<=high;)
    {
        if(arr[i][1] <= arr[j][1])
        {
            new_arr[new_arr_index++] = arr[i][0];
            new_arr[new_arr_index++] = arr[i][1];
            i++;
        }
        else
        {
            new_arr[new_arr_index++] = arr[j][0];
            new_arr[new_arr_index++] = arr[j][1];
            j++;
        }
    }
    
    while(i<=mid)
    {
        new_arr[new_arr_index++] = arr[i][0];
        new_arr[new_arr_index++] = arr[i][1];
        i++;
    }
    
    while(j<=high)
    {
        new_arr[new_arr_index++] = arr[j][0];
        new_arr[new_arr_index++] = arr[j][1];
        j++;
    }
    
    j=low;
    for(i=0; i<new_arr_index; )
    {
        arr[j][0] = new_arr[i++];
        arr[j][1] = new_arr[i++];
        j++;
    }
    free(new_arr);
}


void merge_1d(int * arr, int low, int mid, int high)
{
    int * new_arr = (int *)malloc(sizeof(int) * (high-low+1));
    int new_arr_index = 0;
    
    int i=0,j=0;
    for(i=low, j=mid+1; i<=mid && j<=high;)
    {
        if(arr[i] <= arr[j])
        {
            new_arr[new_arr_index++] = arr[i++];
        }
        else
        {
            new_arr[new_arr_index++] = arr[j++];
        }
    }
    
    while(i<=mid)
    {
        new_arr[new_arr_index++] = arr[i++];
    }
    
    while(j<=high)
    {
        new_arr[new_arr_index++] = arr[j++];
    }
    
    memcpy(&arr[low], &new_arr[0], sizeof(int) * (high-low+1));
    free(new_arr);
}


void merge_sort(int ** arr, int low, int high)
{
    if(low < high)
    {
        int mid = (low+high)/2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}




void merge_sort_1d(int * arr, int low, int high)
{
    if(low<high)
    {
        int mid = (low+high)/2;
        merge_sort_1d(arr, low, mid);
        merge_sort_1d(arr, mid+1, high);
        merge_1d(arr, low, mid ,high);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortByBits(int* arr, int arrSize, int* returnSize)
{
    int * ret_arr = (int *)malloc(sizeof(int) * arrSize);
    int ret_arr_index = 0;
    
    int ** matrix = (int **)malloc(sizeof(int *) * arrSize);
    int matrix_index = 0;
    
    int i=0;
    for(i=0; i<arrSize; i++)
    {
        int * tmp_arr = (int *)malloc(sizeof(int) * 2);
        int tmp_arr_index = 0;
        
        matrix[i] = tmp_arr;
        tmp_arr[0] = arr[i];             //Original value
        
        //No of ones in the number
        int num = arr[i];
        int count = 0;
        int bit_val = 0;
        
        while(num > 0)
        {
            bit_val = (num & 0x01);
            if(bit_val)
            {
                count++;
            }
            num = num>>1;
        }
        
        tmp_arr[1] = count;        //No of ones
    }
    
    merge_sort(matrix, 0, arrSize-1);
    
    for(i=0; i<arrSize; i++)
    {
        ret_arr[ret_arr_index++] = matrix[i][0];

    }
    
    int prev = INT_MIN;
    int start_index = 0;
    int end_index = 0;
    int cur = 0;
    for(i=0; i<arrSize; i++)
    {
        if(prev == INT_MIN)
        {
            prev = matrix[i][1];
            cur = matrix[i][1];
        }
        else
        {
            cur = matrix[i][1];
            if(prev != cur)
            {
                if(start_index != end_index)
                {
                    merge_sort_1d(ret_arr, start_index, end_index);
                    start_index = end_index;
                }
                prev = matrix[i][1];
                start_index++;
                end_index++;
            }
            else if(prev == cur)
            {
                end_index++;
            }
        }
    }
    
    if(start_index != end_index)
    {
        merge_sort_1d(ret_arr, start_index, end_index);
    }
    
    
    *returnSize = ret_arr_index;;
    return ret_arr;
}
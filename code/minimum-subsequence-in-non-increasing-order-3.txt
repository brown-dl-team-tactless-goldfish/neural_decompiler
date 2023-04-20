void merge(int * nums, int low, int mid, int high)
{
    int * ret_arr = (int *)malloc(sizeof(int) * (high - low + 1));
    int ret_arr_index = 0;
    
    int i=0, j=0;
    for(i=low, j=mid+1; i<=mid && j<= high; )
    {
        if(nums[i] <= nums[j])
        {
            ret_arr[ret_arr_index++] = nums[i++];
        }
        else
        {
            ret_arr[ret_arr_index++] = nums[j++];
        }
    }
    
    while(i<=mid)
    {
        ret_arr[ret_arr_index++] = nums[i++];
    }
    
    while(j<=high)
    {
        ret_arr[ret_arr_index++] = nums[j++];
    }
    
    memcpy(&nums[low], &ret_arr[0], sizeof(int) * (high - low + 1));
    free(ret_arr);
}

void merge_sort(int * nums, int low, int high)
{
    if(low < high)
    {
        int mid = (low+high)/2;
        merge_sort(nums, low, mid);
        merge_sort(nums, mid+1, high);
        merge(nums, low, mid, high);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minSubsequence(int* nums, int numsSize, int* returnSize)
{
    int total_sum = 0;
    int i=0;
    for(i=0; i<numsSize; i++)
    {
        total_sum += nums[i];
    }
    
    merge_sort(nums, 0, numsSize-1);
    int total_non_included_sum = total_sum;
    int total_included_sum = 0;
    
    int * ret_arr = (int *)malloc(sizeof(int) * numsSize);
    int ret_arr_index = 0;
    
    for(i=numsSize-1; i>=0; i--)
    {
        total_non_included_sum -= nums[i];
        total_included_sum += nums[i];
        
        if(total_included_sum <= total_non_included_sum)
        {
            ret_arr[ret_arr_index++] = nums[i]; 
        }
        else
        {
            ret_arr[ret_arr_index++] = nums[i]; 
            break;
        }
    }
    
    *returnSize = ret_arr_index;
    return ret_arr;
    
    
}
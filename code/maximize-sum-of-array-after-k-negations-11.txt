void merge(int arr[], int low, int mid, int high)
{
    int * ret_arr = (int *)malloc(sizeof(int)*(high - low + 1));
    int ret_arr_index = 0;
    
    int i=0, j=0;
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
    
    memcpy(&arr[low], ret_arr, sizeof(int) * (high - low + 1));
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

int largestSumAfterKNegations(int* nums, int numsSize, int k)
{
    int i=0;
    bool zero_index = 0;
    int sum = 0;
    int min = INT_MAX;
    
    merge_sort(nums, 0, numsSize-1);
    
    for(i=0; i<numsSize; i++)
    {
        if(nums[i] < 0 && k > 0)
        {
            nums[i] *= -1;
            k--;
        }
        
        if(nums[i] == 0)
        {
            zero_index = true;
        }
        
        if(nums[i] <= min)
        {
            min = nums[i];
        }
        
        sum += nums[i];
    }
    
    if(zero_index || k==0)
        return sum;
    
    if(min > 0)
    {
        if(k%2 != 0)
        {
            sum -= 2*min;
        }
    }
    else if(min < 0)
    {
        if(k%2 != 0)
        {
            sum += 2*min;
        }
    }
    return sum;
    
}
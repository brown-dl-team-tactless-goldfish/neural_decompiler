void merge(int * arr, int low, int mid, int high)
{
    int * ret_arr = (int *)malloc(sizeof(int) * (high - low + 1));
    int ret_arr_index = 0;
    
    int i=0, j=0;
    for(i=low, j=mid+1; i<=mid && j<= high; )
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

void merge_sort(int * arr, int low, int high)
{
    if(low < high)
    {
        int mid = (low + high)/2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}

int largestPerimeter(int* nums, int numsSize)
{
    merge_sort(nums, 0, numsSize-1);
    
    int largest_per = 0;
    int cur_sum = 0;
    //After sorting A[i], A[i+1] and A[i+2], we know that to form a triangle, a+b>c && a+c>b && b+c>a
    //Now A[i+2] is already greater than A[i] & A[i+1], so adding anything to A[i+2] would always be greater that     //3rd side. So we need to check only if A[i] + A[i+1] > A[i+2] ->Triange can be formed
    
    int i=0;
    for(i=0; i<numsSize-2; i++)
    {
        if(nums[i] + nums[i+1] > nums[i+2])
        {
            cur_sum = nums[i] + nums[i+1] + nums[i+2];
            if(cur_sum >= largest_per)
            {
                largest_per = cur_sum;
            }
        }
    }
    return largest_per;
    
}
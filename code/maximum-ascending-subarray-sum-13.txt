

int maxAscendingSum(int* nums, int numsSize)
{
    int current_sum = 0;
    int max_sum = INT_MIN;
    int end_index = 0;
    
    current_sum = nums[0];
    max_sum = current_sum;
    
    for(end_index=1; end_index<numsSize; )
    {
        if(nums[end_index] > nums[end_index-1])
        {
            current_sum += nums[end_index++];
                
            if(current_sum >= max_sum)
            {
                max_sum = current_sum;
            }
        }
        else
        {
            current_sum = nums[end_index++];
            
            if(current_sum >= max_sum)
            {
                max_sum = current_sum;
            }
        }
    }
    
    if(current_sum >= max_sum)
    {
        max_sum = current_sum;
        
    }
    return max_sum;
}
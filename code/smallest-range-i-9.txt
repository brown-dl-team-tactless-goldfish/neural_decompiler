

int smallestRangeI(int* nums, int numsSize, int k)
{
    int max = INT_MIN;
    int min = INT_MAX;
    int ret = 0;
    int i=0;
    for(i=0; i<numsSize; i++)
    {
        if(nums[i] <= min)
        {
            min = nums[i];
        }
    }
    
    for(i=0; i<numsSize; i++)
    {
        if(nums[i] >= max)
        {
            max = nums[i];
        }
    }
    
    int a = min + k;
    int b = max - k;
    
    if(a >= b)
        ret = 0;
    else
        ret = b-a;
        
    return ret;
}
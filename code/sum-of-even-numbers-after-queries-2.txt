

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumEvenAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize)
{
    int even_sum = 0;
    int i=0;
    for(i=0; i<numsSize; i++)
    {
        if(nums[i]%2 == 0)
            even_sum += nums[i];
    }
    
    int * ret_arr = (int *)malloc(sizeof(int) * queriesSize);
    int ret_arr_index = 0;

    for(i=0; i<queriesSize; i++)
    {
        
        int val     = queries[i][0];
        int index   = queries[i][1];

        int prev_val = nums[index];
        nums[index] += val;
        
        if(prev_val%2 == 0 && nums[index]%2 == 0)
        {
            even_sum = even_sum - prev_val + nums[index];
        }
        else if(prev_val%2 == 0 && nums[index]%2 != 0)
        {
            even_sum -= prev_val;
        }
        else if(prev_val%2 !=0 && nums[index]%2 == 0)
        {
            even_sum += nums[index];
        }
        
        ret_arr[ret_arr_index++] = even_sum;
    }
    
    *returnSize = ret_arr_index;
    return ret_arr;
    
}
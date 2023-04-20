

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* buildArray(int* nums, int numsSize, int* returnSize)
{
    int * ret_arr = (int *)malloc(sizeof(int) * numsSize);
    int ret_arr_index = 0;
    
    int i=0;
    for(i=0; i<numsSize; i++)
    {
        ret_arr[ret_arr_index++] = nums[nums[i]];
    }
    
    *returnSize = numsSize;
    return ret_arr;
}
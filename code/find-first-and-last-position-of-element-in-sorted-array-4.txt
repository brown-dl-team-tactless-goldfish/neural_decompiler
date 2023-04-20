

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    
    int *res = calloc(2, sizeof(int));
    *returnSize = 2;
    if(numsSize == 0){ 
        res[0] = -1;
        res[1] = -1;
        return res;
    }
    res[0] = -1;
    res[1] = -1;
    int start = 0;
    int end = numsSize-1;
    int mid;
    //Run binary search two time one for left ind and one for right ind
    
    while(start<=end)
    {
        mid = (start+end)/2;
        if(target<nums[mid])
            end = mid-1;
        else if(target>nums[mid])
            start = mid+1;
        else
        {
            res[0] = mid;
            end = mid-1;
        }
    }
    start = 0;end=numsSize-1;
    while(start<=end)
    {
        mid = (start+end)/2;
        if(target>nums[mid])
            start = mid+1;
        else if(target<nums[mid])
            end = mid-1;
        else
        {
            res[1] = mid;
            start = mid+1;
        }
    }
    return res;
}
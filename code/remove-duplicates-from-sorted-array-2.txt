int removeDuplicates(int* nums, int numsSize)
{
    int i, last = 0;
   
    if (numsSize <= 1) {
        return numsSize;
    }
     
    for (i = 1; i < numsSize; i++) {
        if (nums[i-1] < nums[i]) {
            nums[++last] = nums[i];
        }
    }

    return last+1;
}
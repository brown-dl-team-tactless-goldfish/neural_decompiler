/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize){
    (*returnSize) =numsSize;
    int *res = (int*)malloc((*returnSize)*sizeof(int));
    int i,j;
    for(i=0;i<numsSize;i++) {
        int c = 0;
        for(j=0;j<numsSize;j++) {
            if(j==i) continue;
            if(nums[i]>nums[j]) c++;
        }
        res[i] = c;
    }
    return res;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int* targetIndices(int* nums, int numsSize, int target, int* returnSize){
qsort(nums, numsSize, sizeof(int), cmpfunc);
    int j=0,count=0;
    for(int k=0;k<numsSize;k++)
    {
        if(nums[k]==target)
        {
            count++;
        }
    }
    int *ans=(int*)malloc(sizeof(int)*count);
    *returnSize=count;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]==target)
        {
            ans[j]=i;
            j++;
        }
    }
    return ans;
}
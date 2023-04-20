int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}
int arrayPairSum(int* nums, int numsSize){
qsort(nums, numsSize, sizeof(int), cmpfunc);
    int sums=0;
    for(int i=0;i<numsSize/2;i++)
    {
        sums=sums+nums[i*2];
    }
    return sums;
}
int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int maximumGap(int* nums, int numsSize){
qsort(nums, numsSize, sizeof(int), cmpfunc);
    int max=0;
    if(numsSize<2)
    {
        return 0;
    }
    for(int i=0;i<numsSize-1;i++)
    {
        if(abs(nums[i+1]-nums[i])>max)
        {
            max=abs(nums[i+1]-nums[i]);
        }
    }
    return max;
}
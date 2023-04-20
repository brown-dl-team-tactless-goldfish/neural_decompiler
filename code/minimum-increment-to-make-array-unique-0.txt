int cmp(const void* a, const void* b){
    return *(int*)a - *(int*)b ;
}
int minIncrementForUnique(int* nums, int numsSize){
    qsort(nums, numsSize, sizeof(int), cmp ) ;
    int ans = 0;
    int min = nums[0] ;
    for(int i = 1; i < numsSize; i++){
        if(nums[i] <= min){
            ans += ( min + 1 - nums[i] ) ;
            nums[i] = min + 1 ;
        }
        min = nums[i] ;
    }
    return ans ;
}
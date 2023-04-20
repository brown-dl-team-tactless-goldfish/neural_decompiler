int* singleNumber(int* nums, int numsSize, int* returnSize){
    *returnSize = 2;
    int* ans = calloc(2, sizeof(int));
    long long temp = 0;
    for(int i = 0; i < numsSize; i++){
        temp ^= nums[i];
    }
    temp = temp & -temp;
    
    for(int i = 0; i < numsSize; i++){
        if((temp & nums[i]) == 0)
            ans[0] ^= nums[i];
        else
            ans[1] ^= nums[i];
    }
    return ans;
}
int subarraySum(int* nums, int numsSize, int k){
    int temp[20000000] = {0};
    int idx = 1, sum = 0, count = 0;
    temp[10000000] = 1;
    for(int i=0; i<numsSize; i++)
    {
        sum += nums[i];
        count += temp[sum-k+10000000];
        temp[sum+10000000]++;
    }
    return count;
}
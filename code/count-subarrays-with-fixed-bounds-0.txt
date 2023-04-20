long long countSubarrays(int* nums, int numsSize, int minK, int maxK){

    long long ans = 0;
    int lastminK = -1, lastmaxK = -1;
    int start = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] > maxK || nums[i] < minK)
            start = i + 1;
        if(nums[i] == maxK)
            lastmaxK = i;
        if(nums[i] == minK)
            lastminK = i;

        int pos = fmin(lastmaxK, lastminK);
        if(start > pos)
            continue;
        ans += pos - start + 1 ;
    }
    return ans;
}
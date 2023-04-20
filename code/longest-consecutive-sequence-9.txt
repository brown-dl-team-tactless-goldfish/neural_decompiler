int cmp(void *a, void *b){
    return *(int *)a - *(int *)b;
}

int longestConsecutive(int* nums, int numsSize){
    if(numsSize <= 1) return numsSize;
    
    //sort in non-decreasing order
    qsort(nums, numsSize, sizeof(int), cmp);

    //at least one length
    int count = 1;
    int ret = 1;
    
    for(int i = 1; i < numsSize; i++){
        
        //if the element is duplicate in nums
        if(nums[i] == nums[i-1]){
            continue;
        }
        
        //if the next element is consecutive
        if(nums[i] == nums[i-1] + 1){
            count++;
            ret = ret > count ? ret : count;
        }
        
        //if the next element isn't consecutive
        else{
            count = 1;
        }
    }
    return ret;
}
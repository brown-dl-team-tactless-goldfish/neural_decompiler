int cmpfunc(const void* a, const void* b){
    return *(int*)a - *(int*)b;
}

int specialArray(int* nums, int numsSize){
    int i;
    qsort(nums, numsSize, sizeof(int), cmpfunc);
    
    for(i = 0; i < numsSize; i++){
        if(nums[i] >= (numsSize-i))
            if(i == 0)
                return (numsSize-i) ;
            else{
                if(nums[i-1] < (numsSize-i))
                    return (numsSize-i) ;
            }
    }
    
    return -1;
}
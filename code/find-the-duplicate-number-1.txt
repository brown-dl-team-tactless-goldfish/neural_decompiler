int findDuplicate(int* nums, int numsSize){
    int * count = (int *)calloc(numsSize, sizeof(int));
    for(int i = 0; i < numsSize; i++)
        count[nums[i] - 1]++;
    for(int i = 0; i < numsSize; i++)
        if(count[i] >= 2)
            return i + 1;
    return -1;
}
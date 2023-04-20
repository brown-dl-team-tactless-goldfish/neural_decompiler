int* decompressRLElist(int* nums, int numsSize, int* returnSize){
    int *result = malloc(sizeof(int)*(numsSize/2)*100);
    *returnSize = 0;
    for (int i=0;i<numsSize;i+=2) {
        for (int j = 0;j<nums[i];j++) {
            result[*returnSize] = nums[i+1];
            (*returnSize)++;
        }
    }
    return result;
}

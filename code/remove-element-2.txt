int removeElement(int* nums, int numsSize, int val){
    int validIndex=0,i;
    for(i=0;i<numsSize;i++){
        if(nums[i]!=val){
            nums[validIndex]=nums[i];
            validIndex++;
        }
    }
    return validIndex;
}
int removeElement(int* nums, int numsSize, int val){    
   int j=0;
    for(int i;i<numsSize;i++){
        if(nums[i]!=val){
            nums[j]=nums[i];
            j++;
        }
    }
    return j;
}
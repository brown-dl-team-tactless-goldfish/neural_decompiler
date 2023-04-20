/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize){
    *returnSize=numsSize;
int* a = (int*)malloc(sizeof(int)*numsSize);
int i, n=0, k=1;
for(i=0;i<numsSize;i++){
    if(nums[i]>=0){
        a[n++]=nums[i];
        n++;
    }
    else{
        a[k++]=nums[i];
        k++;
    }
}
return a;
}
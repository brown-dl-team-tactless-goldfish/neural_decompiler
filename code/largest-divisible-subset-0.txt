

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmpfunc(const void* a, const void* b){
    return *(int*)a - *(int*)b;
}
int* largestDivisibleSubset(int* nums, int numsSize, int* returnSize){
    int i, j;
    qsort(nums, numsSize, sizeof(int), cmpfunc);
    
    int* idx = malloc(numsSize * sizeof(int));  //dp record last item
    int* cn = malloc(numsSize * sizeof(int));   //dp record count
    int max = 1;
    int maxId = 0;
    idx[0] = -1;
    cn[0] = 1;
    int temp;
    for(i = 1; i < numsSize; i++){
        idx[i] = -1;
        cn[i] = 1;
        for(j = i-1; j >=0; j--){
            if(nums[i] % nums[j] == 0){
                temp = cn[j] + 1;
                if(temp > cn[i]){
                    cn[i] = temp;
                    idx[i] = j;
                }
            }
        }
        if(cn[i] > max){
            max = cn[i];
            maxId = i;
        }
    }
    * returnSize = max;
    int* ans = malloc(max * sizeof(int));
    for(i = max-1; i >= 0; i--){
        ans[i] = nums[maxId];
        maxId = idx[maxId];
    }
    free(idx);
    free(cn);
    return ans;
}
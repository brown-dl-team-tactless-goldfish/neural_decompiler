#include <stdlib.h>

int cmp(const void *a,const void *b) {
    return *((int*) a) - *((int*) b);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    qsort(nums, numsSize, sizeof(int), cmp);
    (*returnSize) = 0;
    (*returnColumnSizes) = (int*) malloc(sizeof(int) * numsSize * numsSize);
    int **ret = (int**) malloc(sizeof(int*) * numsSize * numsSize);
    for (int i = 0; i < numsSize - 2; i++) {
        if (i == 0 || nums[i] != nums[i-1]) {
            int l = i + 1;
            int r = numsSize - 1;
            while (l < r) {
                if (nums[i] + nums[l] + nums[r] < 0) {
                    l++;
                } else if (nums[i] + nums[l] + nums[r] > 0) {
                    r--;
                } else {
                    ret[(*returnSize)] = (int*) malloc(sizeof(int) * 3);
                    (*returnColumnSizes)[(*returnSize)] = 3;
                    ret[(*returnSize)][0] = nums[i];
                    ret[(*returnSize)][1] = nums[l];
                    ret[(*returnSize)][2] = nums[r];
                    (*returnSize)++;
                    l++;
                    while (l < r && nums[l] == nums[l-1])
                        l++;
                }
            }
        }
    }
    return ret;
}
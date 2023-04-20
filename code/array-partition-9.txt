#include <stdlib.h>

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))

int compare(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int arrayPairSum(int *nums, int numsSize)
{
    qsort(nums, numsSize, sizeof(int), compare);
    int sum = 0;
    for (int i = 0; i < numsSize - 1; i = i + 2)
    {
        sum += MIN(nums[i], nums[i + 1]);
    }
    return sum;
}

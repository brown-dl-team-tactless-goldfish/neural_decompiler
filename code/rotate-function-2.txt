#include <stdio.h>

/* 
 * F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]
 * F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
 *        = 0 * Bk[1] + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
 * thus, we get F(k) - F(k - 1) = sum - nBk[0]
 * then, F(k) = F(k - 1) + sum - nBk[0]
 */

int maxRotateFunction(int* nums, int numsSize){
    int F = 0;
    int sum = 0;
    int max;

    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
        F += i * nums[i];
    }

    max = F;

    for (int i = 1; i < numsSize; i++) {
        /* pay attention to long convertion here! */
        F = F + sum - (long)numsSize * nums[numsSize - i];
        if (F > max)
            max = F;
    }

    return max;
}
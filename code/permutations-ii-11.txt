#ifndef NULL
#define NULL 0
#endif


typedef struct min_max_tuple {
    int min;
    int max;
} min_max ;

min_max range(int* nums, int n) {
    min_max m;
    m.min = nums[0];
    m.max = m.min;
    for (int i = 1; i < n; i++) {
        int k = nums[i];
        if (k > m.max) {
            m.max = k;
        } else if (k < m.min) {
            m.min = k;
        }
    }
    return m;
}

// Return an array of arrays of size *returnSize.
// The sizes of the arrays are returned as *returnColumnSizes array.
// Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    // Initialize a Set type that maps integers to their counts
    min_max r = range(nums, numsSize);
    int min = r.min;
    int max = r.max;
    int* set = (int *) malloc((max - min + 1) * sizeof(int));
    for (int i = 0; i <= max - min; i++) {
        set[i] = 0;
    }
    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        int idx = num - min;
        set[idx] += 1;
    }

    // Initialize the return size, column sizes and output array
    // NOTE: The number of unique permutations will be equal to the number of total permutations
    // divided by the product of count! (where count is the count of any repeated item) over
    // all non-unique items.
    int unique = 1;
    for (int i = numsSize; i > 1; i--) {
        unique = unique * i;
    }
    for (int i = 0; i <= max - min; i++) {
        int count_fact = 1;
        for (int j = set[i]; j > 1; j --) {
            count_fact = count_fact * j;
        }
        unique = unique / count_fact;
    }
    int** out = (int **) malloc(unique * sizeof(int *));
    int* sizes = (int *) malloc(unique * sizeof(int));
    for (int i = 0; i < unique; i++) {
        out[i] = (int *) malloc(numsSize * sizeof(int));
        sizes[i] = numsSize;
    }
    *returnSize = unique;
    *returnColumnSizes = sizes;

    fill(
        out, 0,
        numsSize, unique,
        set, min, max,
        0);

    // Don't forget to free
    free((void *) set);
    return out;
}

// Fill perms[start : end] (start inclusive, end implied).
// rem is the remaining things to add, unique is how many UNIQUE
// numbers are left, remaining is a set of these numbers to their
// counts, min and max ar ethe min and max of that set, and left
// is how far from the left to write to.
void fill(
    int **perms, int start, 
    int rem, int unique,
    int *remaining, int min, int max,
    int left)
{
    // For each remaining unique value to add at this position
    // fill the subtree from there
    for (int i = 0; i <= max - min; i++) {
        int count = remaining[i];
        int num = i + min;
        if (count > 0) {
            // n!/m! => (n-1)!/(m-1)!
            int new_unique = ((unique * count) / rem);
            int end = start + new_unique;
            // TAKE
            remaining[i] --;
            // Fill in the start here
            for (int j = start; j < end; j++) {
                perms[j][left] = num;
            }
            // NOTE: this will not be re-called if all the counts are zero
            fill(
                perms, start,
                rem - 1, new_unique,
                remaining, min, max,
                left + 1);
            // RELEASE
            remaining[i] ++;
            start = end;
        }
    }
}
int findMaxLength(int* nums, int numsSize) {
    int ret = 0;
    int count = 0;
    int arr[numsSize * 2 + 1];
    for (int i = 0; i < numsSize * 2 + 1; i++)
        arr[i] = -2;
    arr[numsSize] = -1;
    for (int i = 0; i < numsSize; i++) {
        count += nums[i] == 0 ? -1 : 1;
        if (arr[count + numsSize] >= -1) {
            if (ret < (i - arr[count + numsSize]))
                ret = i - arr[count + numsSize];
        } else {
            arr[count + numsSize] = i;
        }
    }
    return ret;
}
int wiggleMaxLength(int* nums, int numsSize)
{
    if (numsSize < 2)
        return numsSize;

    int i, len, last;

    for (i = len = 1, last = 0; i < numsSize; i++) {
        if (nums[i] > nums[i - 1])
            if (last == 1)
                ;
            else
                len++, last = 1;
        else if (nums[i] < nums[i - 1])
            if (last == -1)
                ;
            else
                len++, last = -1;
        else
            ;
    }

    return len;
}
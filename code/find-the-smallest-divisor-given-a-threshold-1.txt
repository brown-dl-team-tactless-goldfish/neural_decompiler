int sum(int *nums, int numsSize, int num)
{
    int s = 0;
    for(int i = 0; i < numsSize; i++)
        s += (nums[i] + (num - 1)) / num;
    return s;
}

int smallestDivisor(int* nums, int numsSize, int threshold){
    int left = 1, right = 1000000;
    while(left < right)
    {
        int mid = left + (right - left) / 2;
        if(sum(nums, numsSize, mid) <= threshold)
            right = mid;
        else left = mid + 1;
    }
    return left;
}
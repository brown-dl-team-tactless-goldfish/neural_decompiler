int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    int l=0, r=numsSize-1, mid = r/2;
    *returnSize = 2;
    int* res = malloc(sizeof(int)*2);
    res[0] = -1; res[1] = -1;
    
    while (l <= r)
    {
        mid = l+(r-l)/2;
        if (target == nums[mid]) // might be in both sides
        {
            int mid2 = mid;
            while (l < mid)
            {
                int l_mid = (mid+l)/2;
                if (nums[l_mid] < target)
                    l = l_mid+1;
                
                else
                    mid = l_mid;
            }
            while (mid2 < r)
            {
                int r_mid = (mid2+r+1)/2;
                if (nums[r_mid] >  target)
                    r = r_mid-1;

                else
                    mid2 = r_mid;
            
            }
            res[0] = l; res[1] = r;
            return res;
        }
        else if (target < nums[mid]) // not in right side
            r = mid-1;

        else if (target > nums[mid]) // not in left side
            l = mid+1;
    }
    return res;
}
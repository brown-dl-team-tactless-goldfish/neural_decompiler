int findFinalValue(int* nums, int numsSize, int original){
int z=1,k=0;
    while(z)
    {
        for(int i=0;i<numsSize;i++)
        {
            if(original==nums[i])
            {
                original=original*2;
                k=1;
                break;
            }
        }
        if(k==0)
        {
            z=0;
        }
        k=0;
    }
    return original;
}
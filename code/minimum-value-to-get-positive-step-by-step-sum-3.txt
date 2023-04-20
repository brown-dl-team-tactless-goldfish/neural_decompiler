

int minStartValue(int* nums, int numsSize)
{
    int start_val = 1;
    int start = start_val;
    int i=0;
    int min = INT_MAX;
    int ret_val = 0;
    for(i=0; i<numsSize; i++)
    {
        int new = start_val + nums[i];
        if(new <= min)
        {
            min = new;
        }
        start_val = new;
    }
    
    if(min < 2)
    {
        ret_val = start - min + 1;
    }
    else
    {
        ret_val = start;
    }

    return ret_val;
}
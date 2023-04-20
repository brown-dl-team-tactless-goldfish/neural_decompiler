int hashtable[1001] = {0};

int specialArray(int* nums, int numsSize)
{
    memset(hashtable, 0x00, sizeof(hashtable));
    int x = -1;
    
    int i=0;
    for(i=0; i<numsSize; i++)
    {
        hashtable[nums[i]] += 1;
    }
    int count = 0;
    int j=0;
    
    for(i=0; i<=numsSize; i++)
    {
        count = 0;
        for(j=i; j<1001; j++)
        {
            if(hashtable[j] > 0)
            {
                count += hashtable[j];
            }
            
            if(count > i)
                break;
        }
        
        if(count == i)
            x = i;
    }
    return x;
    
}
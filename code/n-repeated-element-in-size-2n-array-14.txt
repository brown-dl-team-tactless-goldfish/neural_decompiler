int hashtable[10000] = {0};

int repeatedNTimes(int* nums, int numsSize)
{
    memset(hashtable, 0, sizeof(hashtable));
    int ret_element = 0;
    int i=0;
    for(i=0; i<numsSize; i++)
    {
        hashtable[nums[i]] += 1;
        
        if(hashtable[nums[i]] == 2)
        {
            ret_element = nums[i];
        }
    }
    return ret_element;
}
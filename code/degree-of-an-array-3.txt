int hashtable[50000][3] = {0};

int findShortestSubArray(int* nums, int numsSize)
{   
    int i=0;
    
    for(i=0; i<50000; i++)
    {
        hashtable[i][0] = 0;    //freq
        hashtable[i][1] = 0;    //start_index
        hashtable[i][2] = 0;    //end_index
    }
    
    
    for(i=0; i<numsSize; i++)
    {

        if(hashtable[nums[i]][0] == 0)
        {
            hashtable[nums[i]][1] = i;
            hashtable[nums[i]][2] = i;
        }
        else
        {
            hashtable[nums[i]][2] = i;
        } 
        hashtable[nums[i]][0] += 1;
    }
    
    int max = INT_MIN;
    for(i=0; i<50000; i++)
    {
        if(hashtable[i][0] >= max)
        {
            max = hashtable[i][0];
        }
    }
    
    int min_len = INT_MAX;
    int cur_len = 0;
    
    for(i=0; i<numsSize; i++)
    {
        
        if(hashtable[nums[i]][0] == max)
        {
            cur_len = hashtable[nums[i]][2] - hashtable[nums[i]][1];
            if(cur_len <= min_len)
                min_len = cur_len;
        }
    }
    return min_len + 1;
    
    
}
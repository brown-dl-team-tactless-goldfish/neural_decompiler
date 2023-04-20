int hashtable[101] = {0};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* mostVisited(int n, int* rounds, int roundsSize, int* returnSize)
{
    memset(hashtable, 0x00, sizeof(hashtable));
    
    int i=0;
    for(i=1; i<roundsSize; i++)
    {
        int start_sector = rounds[i-1];
        int end_sector   = rounds[i];
        
        if(i == 1)
        {
            start_sector -= 1;
        }
        
        int j=0;
        if(end_sector > start_sector)
        {
            for(j=start_sector+1; j<=end_sector; j++)
            {
                hashtable[j] += 1;
            }   
        }
        else if(end_sector <= start_sector)
        {
            for(j=start_sector+1; j<=n; j++)
            {
                hashtable[j] += 1;
            }
            
            for(j=1; j<=end_sector; j++)
            {
                hashtable[j] += 1;
            }
        }           
    }
    
    int max = INT_MIN;
    for(i=0; i<101; i++)
    {
        if(hashtable[i] >= max)
        {
            max = hashtable[i];
        }
    }
    
    int * ret_arr = (int *)malloc(sizeof(int) * n);
    int ret_arr_index = 0;
   
    for(i=0; i<101; i++)
    {
        if(hashtable[i] == max)
        {
            ret_arr[ret_arr_index++] = i;
        }
    }
    *returnSize = ret_arr_index;
    return ret_arr;
}
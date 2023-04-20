long alice_hashtable[200001] = {0};
long bob_hashtable[200001] = {0};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fairCandySwap(int* aliceSizes, int aliceSizesSize, int* bobSizes, int bobSizesSize, int* returnSize)
{
    memset(alice_hashtable, 0x00, sizeof(alice_hashtable));
    memset(bob_hashtable, 0x00, sizeof(bob_hashtable));
    
    int alice_sum = 0;
    int bob_sum = 0;
    
    int i=0;
    for(i=0; i<aliceSizesSize; i++)
    {
        alice_hashtable[aliceSizes[i]] += 1;
        alice_sum += aliceSizes[i];
    }
    
    for(i=0; i<bobSizesSize; i++)
    {
        bob_hashtable[bobSizes[i]] += 1;
        bob_sum += bobSizes[i];
    }
    
    int * ret_arr = (int *)malloc(sizeof(int) * 2);
    *returnSize = 2;
    
    
    for(i=0; i<aliceSizesSize; i++)
    {
        alice_sum -= aliceSizes[i];
        bob_sum   += aliceSizes[i];
        
        if(bob_sum <= alice_sum)
        {
            alice_sum += aliceSizes[i];
            bob_sum -= aliceSizes[i];
            continue;
        }
        else
        {
            int diff = bob_sum - alice_sum;
            if(diff%2 != 0)
            {
                alice_sum += aliceSizes[i];
                bob_sum -= aliceSizes[i];
                continue; 
            }
            else
            {
                diff = (diff / 2);
                if(bob_hashtable[diff] > 0)
                {
                    ret_arr[0] = aliceSizes[i];
                    ret_arr[1] = diff;
                    break;
                }
                else
                {
                    alice_sum += aliceSizes[i];
                    bob_sum -= aliceSizes[i];
                    continue; 
                }
            }
        }
        
    }
    return ret_arr;
    
    
}
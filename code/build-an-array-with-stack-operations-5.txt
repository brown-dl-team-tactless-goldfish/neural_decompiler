#define TARGET_LEN 101
int target_hash_table[TARGET_LEN] = {0};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** buildArray(int* target, int targetSize, int n, int* returnSize)
{
    memset(target_hash_table, 0x00, sizeof(target_hash_table));
    
    int i=1;
    int max_num = target[targetSize - 1];
    
    char ** ret_arr = (char **)malloc(sizeof(char *)*(2*n));
    int ret_arr_index = 0;
    
    for(i=0; i<targetSize; i++)
    {
        target_hash_table[target[i]] = 1;
    }
    
    for(i=1; i<=max_num; i++)
    {
        if(target_hash_table[i] == 1)
        {
            char * str_arr = (char *)malloc(sizeof(char) * 5);
            ret_arr[ret_arr_index++] = str_arr;
            sprintf(str_arr, "Push");
        }
        
        else 
        {
            char * str_arr = (char *)malloc(sizeof(char) * 5);
            ret_arr[ret_arr_index++] = str_arr;
            sprintf(str_arr, "Push");
            
            str_arr = (char *)malloc(sizeof(char) * 4);
            ret_arr[ret_arr_index++] = str_arr;
            sprintf(str_arr, "Pop");
        }
    }
    *returnSize = ret_arr_index;
    return ret_arr;
}
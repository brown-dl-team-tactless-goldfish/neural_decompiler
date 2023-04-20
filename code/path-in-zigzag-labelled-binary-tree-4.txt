int find_row(label)
{
    return (log(label)/log(2))+1;   
}

int find_parent(int level, int label)
{
    int max_val = pow(2, level)-1;
    int min_val = pow(2, level-1);
    
    int parent = ((max_val + min_val) - label)/2;
    
    return parent;
}



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pathInZigZagTree(int label, int* returnSize)
{
    
    int label_level = find_row(label);
    
    int * ret_arr = (int *)malloc(sizeof(int) * label_level);
    int ret_arr_index;
     *returnSize = label_level;
    int row_size = label_level;
    
    ret_arr[ret_arr_index++] = label;
    
    if(label == 1)
    {
        return ret_arr;
    }
    
    int parent = find_parent(label_level--, label);
    label = parent;
    ret_arr[ret_arr_index++] = label;
    
    while(label_level > 1)
    {
        parent = find_parent(label_level--, label);
        label = parent;
        ret_arr[ret_arr_index++] = label;
    }
    
    int i=0;
    for(i=0; i<(row_size/2);i++)
    {
        int tmp = 0;
        tmp = ret_arr[i];
        ret_arr[i] = ret_arr[(row_size-1)-i];
        ret_arr[(row_size-1)-i] = tmp;
    }
    
   
    return ret_arr;
    
}
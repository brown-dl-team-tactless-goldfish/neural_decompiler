struct Node
{
    int x_cor;
    int y_cor;
    struct Node * next;
};

struct Node * hashtable[201] = {NULL};


void insert_hashtable(int x, int y, int diff)
{
    struct Node * new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->x_cor = x;
    new_node->y_cor = y;
    new_node->next = NULL;
    
    
    struct Node * trav_ptr = hashtable[diff];
    if(trav_ptr == NULL)    //Entry is empty
    {
        hashtable[diff] = new_node;
    }
    else
    {
        while(trav_ptr->next != NULL)
        {
            trav_ptr = trav_ptr->next;
        }
        
        trav_ptr->next = new_node;
    }
}


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** allCellsDistOrder(int rows, int cols, int rCenter, int cCenter, int* returnSize, int** returnColumnSizes)
{
    int i=0;
    for(i=0; i<201; i++)
    {
        hashtable[i] = NULL;
    }
    
    
    int ** ret_arr = (int **)malloc(sizeof(int *) * (rows * cols));
    int ret_arr_index = 0;
    
    int * ret_col = (int *)malloc(sizeof(int) * (rows * cols));
    int ret_col_index = 0;
    
    
    int j=0;
    for(i=0; i<rows; i++)
    {
        for(j=0; j<cols; j++)
        {       
            int x_diff = (rCenter - i);
            if(x_diff < 0)
            {
                x_diff *= -1;
            }
            
            int y_diff = (cCenter - j);
            if(y_diff < 0)
            {
                y_diff *= -1;
            }
            int diff = x_diff + y_diff;
            
            insert_hashtable(i, j, diff);
        }
    }
    
   int hash_index = 0; 
   struct Node * trav_ptr = hashtable[hash_index++];

   for(i=0; i<(rows*cols); i++)
   {
      int * arr = (int *)malloc(sizeof(int) * 2); 
      
       if(trav_ptr!=NULL)
       {
          arr[0] = trav_ptr->x_cor;
          arr[1] = trav_ptr->y_cor;
          trav_ptr = trav_ptr->next;

          ret_arr[ret_arr_index++] = arr;
          ret_col[ret_col_index++] = 2;
       }
       
       if(trav_ptr == NULL)
       {
           trav_ptr = hashtable[hash_index++];
       }
       
   }
    
    *returnSize = ret_arr_index;
    *returnColumnSizes = ret_col;
    return ret_arr;
}
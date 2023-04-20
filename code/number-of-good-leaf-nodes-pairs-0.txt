/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int total_count = 0;

int * count(struct TreeNode * root, int distance, int * arr_index)
{
    if(root == NULL)
        return;
    
    int left_arr_index = 0;
    int right_arr_index = 0;
    
    int * left_arr  = count(root->left, distance, &left_arr_index);
    int * right_arr = count(root->right, distance, &right_arr_index);
    
    if(root->left==NULL && root->right==NULL)
    {
        int * ret_arr = (int *)malloc(sizeof(int) * 1);
        ret_arr[0] = 1;
        *arr_index = 1;
        return ret_arr;
    }
    
    
    int * tmp_arr = (int *)malloc(sizeof(int) * (left_arr_index + right_arr_index));
    int tmp_arr_index = 0;
    int i=0;
    for(i=0; i<left_arr_index; i++)
    {
        tmp_arr[tmp_arr_index++] = left_arr[i];
    }
   
    for(i=0; i<right_arr_index; i++)
    {
        tmp_arr[tmp_arr_index++] = right_arr[i];    
    }

    //Check whether any of the pair satisfies the condition
    int j=0;
    for(i=0; i<left_arr_index; i++)
    {
        for(j=left_arr_index; j<left_arr_index + right_arr_index; j++)
        {
            if(tmp_arr[i] + tmp_arr[j] <= distance)
            {
                total_count++;
            }
        }
    }
    *arr_index = tmp_arr_index;
    
    for(i=0; i<tmp_arr_index; i++)
    {
        tmp_arr[i] += 1;
    }
    free(left_arr);
    free(right_arr);
    
    return tmp_arr;
    
}

int countPairs(struct TreeNode* root, int distance)
{
    total_count = 0;
    int arr_index = 0;
    int * ret = count(root, distance, &arr_index);
    return total_count;
}
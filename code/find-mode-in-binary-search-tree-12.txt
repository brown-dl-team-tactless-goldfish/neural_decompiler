/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int count_nodes(struct TreeNode * root)
{
    if(root == NULL)
        return 0;
    
    return (1 + count_nodes(root->left) + count_nodes(root->right));
}

void inorder(struct TreeNode * root, int * ret_arr, int * ret_arr_index)
{
    if(root == NULL)
        return;
    
    inorder(root->left, ret_arr, ret_arr_index);
    ret_arr[(*ret_arr_index)++] = root->val;
    inorder(root->right, ret_arr, ret_arr_index);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMode(struct TreeNode* root, int* returnSize)
{
    int nodes = count_nodes(root);
    int * ret_arr = (int *)malloc(sizeof(int) * nodes);
    int ret_arr_index = 0;
    
    inorder(root, ret_arr, &ret_arr_index);
    
    //ret_arr contains sorted elements in increasing order
    int max_count = INT_MIN;
    
    int start_index = 0;
    int prev_element = ret_arr[0];
    int end_index = 1;
    
    for(end_index=1; end_index<nodes; )
    {
        if(ret_arr[end_index] == prev_element)
        {
            end_index++;
        }
        else
        {
            int diff = end_index - start_index;
            if(diff >= max_count)
            {
                max_count = diff;
            }
            start_index = end_index;
            prev_element = ret_arr[start_index];
            end_index++;
        }
    }
    
    int diff = end_index-start_index;
    if(diff >= max_count)
    {
        max_count = diff;
    }
    printf("%d", max_count);
    
    int * new_arr = (int *)malloc(sizeof(int)*nodes);
    int new_arr_index = 0;
    
    start_index = 0;
    prev_element = ret_arr[0];
    for(end_index=1; end_index<nodes;)
    {
        if(ret_arr[end_index] == prev_element)
        {
            end_index++;
        }
        else
        {
            int diff = end_index - start_index;
            if(diff == max_count)
            {
                new_arr[new_arr_index++] = prev_element;
            }
            start_index = end_index;
            prev_element = ret_arr[start_index];
            end_index++;
        }
    }
    
    diff = end_index-start_index;
    if(diff == max_count)
    {
        new_arr[new_arr_index++] = prev_element;
    }
        
        
    *returnSize = new_arr_index;    
    return new_arr;
}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void inorder(struct TreeNode * root, int * ret_arr, int * ret_arr_index)
{
    if(root == NULL)
        return;
    
    inorder(root->left, ret_arr, ret_arr_index);
    ret_arr[(*ret_arr_index)++] = root->val;
    inorder(root->right, ret_arr, ret_arr_index);
}

int count(struct TreeNode * root)
{
    if(root==NULL)
        return 0;
    
    return (1 + count(root->left) + count(root->right));
}

int minDiffInBST(struct TreeNode* root)
{
    int no_of_nodes = count(root);
    int * ret_arr = (int *)malloc(sizeof(int) * no_of_nodes);
    int ret_arr_index = 0;
    inorder(root, ret_arr, &ret_arr_index);
    
    int min_diff = INT_MAX;
    int i=0;
    for(i=0; i<no_of_nodes-1; i++)
    {
        int diff = ret_arr[i+1] - ret_arr[i];
        if(diff < min_diff)
        {
            min_diff = diff;
        }
    }
    return min_diff;
}
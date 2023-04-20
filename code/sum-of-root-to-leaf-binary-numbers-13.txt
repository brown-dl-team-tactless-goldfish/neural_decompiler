/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void sum(struct TreeNode * root, int current_sum, int * total_sum)
{
    if(root == NULL)
        return;
    
    if((root->left == NULL) && (root->right == NULL))
    {
        *total_sum += (current_sum << 1)|(root->val);
    }
    
    sum(root->left,  (current_sum << 1)|(root->val), total_sum);
    sum(root->right, (current_sum << 1)|(root->val), total_sum);
    
    
}

int sumRootToLeaf(struct TreeNode* root)
{
    int current_sum = 0;
    int total_sum = 0;
    
    sum(root, 0, &total_sum);
    return total_sum;
}
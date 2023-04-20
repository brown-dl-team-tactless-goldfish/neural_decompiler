/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int traversal(struct TreeNode * root, int * count)
{
    if(root == NULL)
        return 0;
    
    int left_count = traversal(root->left, count);
    int right_count = traversal(root->right, count);
    
    if(root->left==NULL && root->right==NULL)
    {
        if(root->val == 0)
        {
            *count += 1;
            return -1;
        }
        else if(root->val == 1)
        {
            return 0;
        }
        else
        {
            *count += (root->val - 1);
            return (root->val - 1);
        }
    }

    int data = (root->val - 1 + left_count + right_count);
    if(data < 0)
        data *= -1;
    *count += data;
    return (root->val - 1 + left_count + right_count);    
    
}


int distributeCoins(struct TreeNode* root)
{
    int count = 0;
    traversal(root, &count);
    return count;
}
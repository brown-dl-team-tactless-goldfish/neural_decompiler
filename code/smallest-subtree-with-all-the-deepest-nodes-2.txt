/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int find_height(struct TreeNode * root)
{
    if(root == NULL)
        return 0;
    
    int left = find_height(root->left);
    int right = find_height(root->right);
    
    if(left >= right)
        return left+1;
    else
        return right+1;
}

struct TreeNode * find_subtree(struct TreeNode * root, int ht, int cur_ht)
{
    if(root == NULL)
        return;
    
    
    struct TreeNode * left = find_subtree(root->left,  ht, cur_ht+1);
    struct TreeNode * right = find_subtree(root->right, ht, cur_ht+1);
   
    if(cur_ht == ht && root->left == NULL && root->right == NULL)
    {
        return root;
    }
    
   if(left!=NULL && right!=NULL)
       return root;
    else if(left!=NULL && right==NULL)
        return left;
    else if(right!=NULL && left==NULL)
        return right;
    
    return NULL;
}

struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root)
{
    int height = find_height(root);
    
    return find_subtree(root, height, 1);
}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int height_of_tree(struct TreeNode * root)
{
    if(root == NULL)
        return 0;
    
    int left = height_of_tree(root->left);
    int right = height_of_tree(root->right);
    
    if(left >= right)
        return left+1;
    else
        return right+1;

}


int preorder(struct TreeNode * root, int cur_level, int height)
{
    if(root == NULL)
        return 0;
    
    if(cur_level == height)
        return root->val;
    
    
    int left = preorder(root->left, cur_level+1, height);
    int right = preorder(root->right, cur_level+1, height);
    
    return left+right;
}
    
int deepestLeavesSum(struct TreeNode* root)
{
    int height = height_of_tree(root);

    int sum = preorder(root, 1, height);
    return sum;
}
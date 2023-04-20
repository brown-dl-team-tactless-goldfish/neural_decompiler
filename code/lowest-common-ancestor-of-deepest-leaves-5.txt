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
        return (left + 1);
    else
        return (right+1);
}

void find_deepest_node(struct TreeNode * root, int cur_ht, int max_ht, bool * found)
{
    if(root == NULL)
        return;
    
    if(cur_ht == max_ht)
    {
        *found = true;
        return;
    }
    
    find_deepest_node(root->left, cur_ht+1, max_ht, found);
    find_deepest_node(root->right, cur_ht+1, max_ht, found);
}

void preorder(struct TreeNode * root, int height, int cur_ht, struct TreeNode ** common)
{
    if(root == NULL)
        return;
    
    //If the nodes has the deepest leaves on both subtrees then the node itself is the common ancestor
    bool left_found = false;
    bool right_found = false;
    
    find_deepest_node(root->left,  cur_ht+1, height, &left_found);
    find_deepest_node(root->right, cur_ht+1, height, &right_found);
    
    if((left_found==true) && (right_found==true))
    {
        *common = root;
        return;
    }
    else
    {
        
        if(*common == NULL)
            preorder(root->left, height, cur_ht+1, common);
        
        if(*common == NULL)
            preorder(root->right, height, cur_ht+1, common);
    }
        
}

void find_deep_leaf_addr(struct TreeNode * root, int height, int cur_ht, struct TreeNode ** common)
{
    if(root == NULL)
        return;
    
    if(cur_ht == height)
    {

        *common = root;
        return;
    }
    
    find_deep_leaf_addr(root->left,  height, cur_ht+1, common);
    find_deep_leaf_addr(root->right, height, cur_ht+1, common);
}

struct TreeNode* lcaDeepestLeaves(struct TreeNode* root)
{
    int height = find_height(root);
    struct TreeNode * common = NULL;
    int cur_ht = 1;
    
    preorder(root, height, cur_ht, &common);

    if(common == NULL)
    {

        find_deep_leaf_addr(root, height, cur_ht, &common);
    }
    return common;
}
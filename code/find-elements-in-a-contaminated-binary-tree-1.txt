/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */



typedef struct {
    struct TreeNode * root_node;
} FindElements;

void preorder(struct TreeNode * root, int prev_node_val, bool left)
{
    if(root == NULL)
        return;
    
    if(prev_node_val == INT_MIN)
    {
        root->val = 0;
    }
    else
    {
        if(left == true)
        {
            root->val = (2*prev_node_val)+1;
        }
        else
        {
            root->val = (2*prev_node_val)+2;
        }
    }
    
    preorder(root->left, root->val, true);
    preorder(root->right, root->val, false);
}


FindElements* findElementsCreate(struct TreeNode* root) 
{
    int prev_node_val;
    FindElements * ret = (FindElements *)malloc(sizeof(FindElements));
    ret->root_node = root;
    
    preorder(root, INT_MIN, false);
    return ret;
}

void find(struct TreeNode * root, int target, bool * target_found)
{
    if(root==NULL)
        return;
    
    if(root->val == target)
    {
        *target_found = true;
        return;
    }
    
    find(root->left, target, target_found);
    find(root->right, target, target_found);
}

bool findElementsFind(FindElements* obj, int target) 
{
    struct TreeNode * root = obj->root_node;
    bool target_found = false;
    find(root, target, &target_found);
    return target_found;
}

void findElementsFree(FindElements* obj) 
{
    free(obj);
}

/**
 * Your FindElements struct will be instantiated and called as such:
 * FindElements* obj = findElementsCreate(root);
 * bool param_1 = findElementsFind(obj, target);
 
 * findElementsFree(obj);
*/
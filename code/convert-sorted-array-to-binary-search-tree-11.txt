/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int height(struct TreeNode * root)
{
    if(root == NULL)
        return 0;
    
    int left = height(root->left);
    int right = height(root->right);
    
    if(left >= right)
        return left+1;
    return right+1;
}

int calculate_bf(struct TreeNode * root)
{
    int balance_factor = 0;
    
    if(root->left == NULL && root->right == NULL)
    {
        balance_factor = 0;
    }
    else if(root->left == NULL && root->right != NULL)
    {
        balance_factor = 0 - (height(root->right));
    }
    else if(root->left != NULL && root->right == NULL)
    {
        balance_factor = height(root->left);
    }
    else
    {
       balance_factor = height(root->left) - height(root->right); 
    }
    return balance_factor;
}

struct TreeNode * r_insert(struct TreeNode * root, int element)
{
    if(root == NULL)
    {
        struct TreeNode * new_node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
        new_node->val   = element;
        new_node->left  = NULL;
        new_node->right = NULL;
        return new_node;
    }
    else
    {
        if(element < root->val)
        {
            root->left = r_insert(root->left, element);
        }
        else if(element > root->val)
        {
            root->right = r_insert(root->right, element);
        }
        
        //Calculate the balance factor
        int balance_factor = calculate_bf(root);
        
        if(balance_factor >= 2 || balance_factor <= -2)
        {
                //Only RR Rotation is required
                struct TreeNode * tmp_ptr = root;
                struct TreeNode * right_ptr = root->right;
                tmp_ptr->right = right_ptr->left;
                right_ptr->left = tmp_ptr;
                return right_ptr;

        }
    }
    return root;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize)
{
    int i=0;
    
    struct TreeNode * root = NULL;
    
    //Insert the nodes in the tree
    for(i=0; i<numsSize; i++)
    {
        root = r_insert(root, nums[i]);
    }
    return root;
    
}
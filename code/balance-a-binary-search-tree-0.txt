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
    if(root==NULL)
        return 0;
    
    int left = height(root->left);
    int right = height(root->right);
    
    if(left>=right)
        return left+1;
    
    return right+1;
}

int check_balance_factor(struct TreeNode * root)
{
    int balance_factor = 0;
    if(root->left==NULL && root->right==NULL)
    {
        balance_factor = 0;
    }
    else if(root->left==NULL && root->right!=NULL)
    {
        balance_factor = 0 - height(root->right);
    }
    else if(root->left!=NULL && root->right==NULL)
    {
        balance_factor = height(root->left);
    }
    else
    {
        balance_factor = height(root->left) - height(root->right);
    }
    return balance_factor;
}

struct TreeNode* balance(struct TreeNode * root, bool * bal)
{
        if(root == NULL)
        return;
    
    root->left  = balance(root->left, bal);
    root->right = balance(root->right, bal);
    
    //Check the balance factor
    int bal_factor = check_balance_factor(root);
    //printf("node : %d, bf : %d\r\n", root->val, bal_factor);
    if(bal_factor>=2 || bal_factor <= -2)
    {
        *bal = false;
        //LL Rotation
        if(bal_factor>=2 && check_balance_factor(root->left)>=0)
        {
            struct TreeNode * tmp_node = root;
            struct TreeNode * left_node = root->left;
            
            tmp_node->left = left_node->right;
            left_node->right = tmp_node;
            return left_node;
        }
         
        //RR Rotation
        else if(bal_factor<=-2 && check_balance_factor(root->right)<=0)
        {
            struct TreeNode * tmp_node = root;
            struct TreeNode * right_node = root->right;
            
            tmp_node->right = right_node->left;
            right_node->left = tmp_node;
            return right_node;
        }
                     
        //LR Rotation
        else if(bal_factor>=2 && check_balance_factor(root->left)<=0)
        {
            struct TreeNode * tmp_node = root;
            struct TreeNode * left_node = root->left;
            struct TreeNode * new_node = left_node->right;
            
            tmp_node->left = new_node->right;
            left_node->right = new_node->left;
            new_node->left = left_node;
            new_node->right = tmp_node;
            return new_node;
        }
        
        //RL Rotation
        else if(bal_factor<=-2 && check_balance_factor(root->right)>=0)
        {
            struct TreeNode * tmp_node = root;
            struct TreeNode * right_node = root->right;
            struct TreeNode * new_node = right_node->left;
            
            tmp_node->right = new_node->left;
            right_node->left = new_node->right;
            new_node->right = right_node;
            new_node->left = tmp_node;
            return new_node;
        }
    }
    return root;
}

struct TreeNode* balanceBST(struct TreeNode* root)
{
    bool bal = false;
    
    while(bal == false)
    {
        bal = true;
        root = balance(root, &bal);
    }
    return root;
}
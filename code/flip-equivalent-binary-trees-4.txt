/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void flip(struct TreeNode * root1, struct TreeNode * root2, bool * match)
{
    if(root1==NULL && root2==NULL)
    {
        return;
    }
    
    if(root1==NULL || root2==NULL)
    {
        *match = false;
        return;
    }
    
    if(root1->val != root2->val)
    {
        *match = false;
        return;
    }
    
    if(root1->left!=NULL && root1->right!=NULL && root2->left != NULL && root2->right != NULL)
    {
        if(root1->left->val == root2->left->val && root1->right->val == root2->right->val)
        {
            flip(root1->left, root2->left, match);
            flip(root1->right, root2->right, match);
        }
        else if(root1->left->val == root2->right->val && root1->right->val == root2->left->val)
        {
            flip(root1->left, root2->right, match);
            flip(root1->right, root2->left, match);
        }
        else
        {
            *match = false;
            return;
        }
    }
    else
    {
        if(root1->left == NULL && root2->left == NULL && root1->right!=NULL && root2->right!=NULL)
        {
            if(root1->right->val == root2->right->val)
                flip(root1->right, root2->right, match);
            else
            {
                *match = false;
                return;
            }
                
        }
        else if(root1->left == NULL && root2->right == NULL && root1->right!=NULL && root2->left!=NULL)
        {
            if(root1->right->val == root2->left->val)
                flip(root1->right, root2->left, match);
            else
            {
                *match = false;
                return;
            }
        }
        else if(root1->right == NULL && root2->right == NULL && root1->left!=NULL && root2->left!=NULL)
        {
            if(root1->left->val == root2->left->val)
                flip(root1->left, root2->left, match);
            else
            {
                *match = false;
                return;
            }
        }
        else if(root1->right == NULL && root2->left == NULL && root1->left!=NULL && root2->right!=NULL)
        {
            if(root1->left->val == root2->right->val)
                flip(root1->left, root2->right, match);
            else
            {
                *match = false;
                return;
            }
        }
        else if(root1->left == NULL && root2->left == NULL && root1->right == NULL && root2->right == NULL)
        {
            return;
        }
        else
        {
            *match = false;
            return;
        }
    }
    
}

bool flipEquiv(struct TreeNode* root1, struct TreeNode* root2)
{
    bool match = true;
    flip(root1, root2, &match);
    return match;
}
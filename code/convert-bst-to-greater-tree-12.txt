struct TreeNode* convertBST(struct TreeNode* root){
    int sum = 0;
    struct TreeNode *cur = root, *pre;

    while(cur)
    {
        if(cur->right == NULL)
        {
            sum = cur->val = sum + cur->val;
            cur = cur->left;
        }
        else
        {
            pre = cur->right;
            while(pre->left != cur && pre->left != NULL)
                pre = pre->left;

            if(pre->left == NULL)
            {
                pre->left = cur;
                cur = cur->right;
            }
            else
            {
                sum = cur->val = cur->val + sum;
                pre->left = NULL;
                cur = cur->left;
            }
            
        }
    }
    return root;
}
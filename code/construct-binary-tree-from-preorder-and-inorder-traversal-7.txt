struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    if (preorderSize == 0) return NULL;
    
    struct TreeNode* root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = *preorder;
    
    int i = 0;
    while (inorder[i] != *preorder) ++i;
    root->left = buildTree(preorder + 1, i, inorder, i);
    root->right = buildTree(preorder + 1 + i, preorderSize - i - 1,
                            inorder + 1 + i, inorderSize - i - 1);
    
    return root;
}
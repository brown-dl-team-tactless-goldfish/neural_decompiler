void minDiffInBSTUtil(struct TreeNode *node, struct TreeNode **prev, int *minDiff) {
    if(!node) return;
    
    minDiffInBSTUtil(node->left, prev, minDiff);
    if(*prev != NULL) 
        *minDiff = fmin(*minDiff, node->val - (*prev)->val);
        
    *prev = node;
    minDiffInBSTUtil(node->right, prev, minDiff);        
}

int minDiffInBST(struct TreeNode* root){
    int minDiff = INT_MAX;
    struct TreeNode *prev = NULL;
    minDiffInBSTUtil(root, &prev, &minDiff);
    return minDiff;
}
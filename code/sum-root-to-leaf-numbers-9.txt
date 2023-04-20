void sumRootToLeaf(struct TreeNode* root, int rootVal, int* sum){
    if(!root->left && !root->right){
        *sum+=(rootVal);
        return;
    }
    
    if(root->left){
        sumRootToLeaf(root->left, 10*rootVal + root->left->val, sum);
    }
    if(root->right){
        sumRootToLeaf(root->right, 10*rootVal + root->right->val, sum);
    }
    
}

int sumNumbers(struct TreeNode* root){
    
    int sum = 0;
    if(!root){
        return sum;
    }
    sumRootToLeaf(root, root->val, &sum);
    return sum;
    
}
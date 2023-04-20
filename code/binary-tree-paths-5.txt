void TreePaths(struct TreeNode* root, char** ret, int* returnSize){
    
    if(!root->left && !root->right){
        ret[*returnSize] = calloc(610, sizeof(char));
        sprintf(ret[*returnSize], "%d", root->val);
        (*returnSize)++;
        return;
    }
    
    int i=0;
    if (root->left){
        i = *returnSize;
        TreePaths(root->left, ret, returnSize);
        char tmp[610] = {};
        for(;i < *returnSize; i++){
            sprintf(tmp,"%d->%s", root->val, ret[i]);
            sprintf(ret[i], "%s", tmp);
        }
    }
    
    if (root->right){
        i = *returnSize;
        TreePaths(root->right, ret, returnSize);
        char tmp[610] = {};
        for(;i < *returnSize; i++){
            sprintf(tmp,"%d->%s", root->val, ret[i]);
            sprintf(ret[i], "%s", tmp);
        }
    }
    
}

char ** binaryTreePaths(struct TreeNode* root, int* returnSize){
    char **ret = malloc(sizeof(char*)*100);
    int size, i;
    *returnSize = 0;
    
    TreePaths(root, ret, returnSize);
    return ret;
}
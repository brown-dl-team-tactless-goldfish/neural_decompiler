void reverse(char *s, int l, int r) {
    while(l < r) {
        char c = s[l];
        s[l] = s[r];
        s[r] = c;
        l++, r--;
    }
}

void dfs(struct TreeNode *node, char *curPath, int *i, char *res) {
    if(!node) return;
    curPath[(*i)++] = node->val + 'a';
    
    if(!node->left && !node->right) {
        curPath[(*i)] = '\0';
        
        reverse(curPath, 0, (*i) - 1);
        if(strlen(res) == 0)
            strcpy(res, curPath);
        
        if(strcmp(res, curPath) > 0) {
            
            strcpy(res, curPath);
        }
        reverse(curPath, 0, (*i) - 1);
    }
    dfs(node->left, curPath, i, res);
    dfs(node->right, curPath, i, res);
    --*i;
}

char * smallestFromLeaf(struct TreeNode* root){
    char *curStr = calloc(sizeof(char), 100);
    char *res = calloc(sizeof(char), 100);
    int idx = 0;
    
    dfs(root, curStr, &idx, res);
    return res;
}
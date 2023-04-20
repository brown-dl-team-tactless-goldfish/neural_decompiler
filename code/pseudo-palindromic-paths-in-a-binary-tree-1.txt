int DFS(struct TreeNode* root, int* hashTable, int hashSize){    
    hashTable[root->val]++;
    if(root->left == NULL && root->right== NULL){        
        int odd = 0;
        for(int i = 0; i < hashSize; i++){
            if(hashTable[i] % 2){
                odd++;
                if(odd > 1)
                    return 0;
            }
        }
        return 1;
    }
    
    int LeftCn = 0, RightCn = 0;
    if(root->left){
        LeftCn= DFS(root->left, hashTable, hashSize);
        hashTable[root->left->val]--;   
    }
    if(root->right){
        RightCn = DFS(root->right, hashTable, hashSize);
        hashTable[root->right->val]--;   
    }
    
    return LeftCn + RightCn;
}

int pseudoPalindromicPaths (struct TreeNode* root){
    int  hashSize = 10;
    int* hashTable = calloc(hashSize , sizeof(int));    
    return DFS(root, hashTable, hashSize);
}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void nums(struct TreeNode* root, int* num, int* cnt){
    if(root){
        num[(*cnt)++]=root->val;
        nums(root->left, num, cnt);
        nums(root->right, num, cnt);
    }    
    return;
}

bool findTarget(struct TreeNode* root, int k){
    int *cnt = calloc(1, sizeof(int)), *num = malloc(10000*sizeof(int));
    
    nums(root, num, cnt);
    for(int i=0; i<(*cnt); i++){
        for(int j=i+1; j<(*cnt); j++){
            if(num[i]+num[j]==k)
                return true;
        }    
    }
    return false;
}
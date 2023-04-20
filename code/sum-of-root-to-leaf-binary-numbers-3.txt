/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


void dfs(struct TreeNode* root,int *num,int cur){
    if(!root){
        return;
    }else{
        if(root->val==1) cur=cur*2+1;
        else cur=cur*2;
        if(root->right==NULL && root->left==NULL){
            (*num)+=cur;
        }
        dfs(root->left,num,cur);
        dfs(root->right,num,cur);
    }
}

int sumRootToLeaf(struct TreeNode* root){
    int num=0;
    dfs(root,&num,0);
    return num;
}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void find(struct TreeNode* root,int *maxdepth,int depth,int *val){
    if(!root) return;
    if(*maxdepth < depth){
        *maxdepth=depth;
        *val=root->val;
    }
    find(root->left,maxdepth,depth+1,val);
    find(root->right,maxdepth,depth+1,val);
}

int findBottomLeftValue(struct TreeNode* root){
    int maxdepth=-1;
    int val=0;
    find(root,&maxdepth,0,&val);
    return val;
}
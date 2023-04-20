/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool dfs(struct TreeNode* root,int target) {
    if(root->left) {
        if(dfs(root->left,target)) root->left = NULL;
    } 
    if(root->right) {
        if(dfs(root->right,target)) root->right = NULL;
    }
    if(!root->left && !root->right && root->val == target){
        free(root);
        return true;
    }
    return false;
}

struct TreeNode* removeLeafNodes(struct TreeNode* root, int target){
    if(!root) return root;
    if(dfs(root,target)) root=NULL;
    return root;
}
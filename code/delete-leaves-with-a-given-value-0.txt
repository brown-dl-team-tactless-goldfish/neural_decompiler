/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* removeLeafNodes(struct TreeNode* root, int target){
if (root==NULL) return NULL;
// First see if we've got nodes to delete among the children
root->left = removeLeafNodes(root->left,target);
root->right = removeLeafNodes(root->right,target);
// And then, when we check here, we'll know if this node gets deleted too
if ((root->left==NULL) && (root->right==NULL) && (root->val==target))
    return NULL;
return root;
}
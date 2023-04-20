/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool evaluateTree(TreeNode* root) {
        if(root->left==NULL && root->right==NULL) {
            //leaf node
            return(root->val==1? true:false);
        }
        bool left=evaluateTree(root->left); //left subtree
        bool right=evaluateTree(root->right); //right subtree
        if(root->val==2) {
            //or operator
            return(left || right);
        }
        if(root->val==3) {
            //and operator
            return(left && right);
        }
        return false;
    }
};
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> helper(TreeNode *root, int &ans) {
        if(!root)
            return {};
        vector<int> v = {root->val, root->val};
        if(root->left) {
            vector <int> l = helper(root->left, ans);
            ans = max(ans, max(abs(root->val - l[0]), abs(root-> val - l[1])));
            v[0] = min(v[0], l[0]);
            v[1] = max(v[1], l[1]);
        }
        
        if(root->right) {
            vector <int> r = helper(root->right, ans);
            ans = max(ans, max(abs(root->val - r[0]), abs(root-> val - r[1])));
            v[0] = min(v[0], r[0]);
            v[1] = max(v[1], r[1]);
        }
        return v;
            
    }
    int maxAncestorDiff(TreeNode* root) {
        int ans = 0;
        helper(root, ans);
        return ans;
    }
};
class Solution {
public:
    int ans;
    int dfs(TreeNode* root) {
        if(!root) return 0;
        int l = dfs(root->left);
        int r = dfs(root->right);
        
        root->val += l + r;
        ans += abs(root->val - 1);
        return root->val - 1;
    }
    int distributeCoins(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
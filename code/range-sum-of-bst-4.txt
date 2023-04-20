class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        int sum = 0;
        helper(root, L, R, sum);
        return sum;
    }
    void helper(TreeNode* root, int L, int R, int &sum){
        if(!root) return;
        if(root->val >= L && root->val <= R)
            sum += root->val;
        helper(root->left, L, R, sum);
        helper(root->right, L, R, sum);
    }
};
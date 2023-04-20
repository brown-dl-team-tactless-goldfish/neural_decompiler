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
    int getheight(TreeNode *root)
{
    if (!root)
        return 0;
    return max(getheight(root->left), getheight(root->right)) + 1;
}

void chalochalo(TreeNode *root, int si, int ei, int h, vector<vector<string>> &v)
{
    if(root == NULL) return;
    if(si > ei) return;
    int mid = (si + ei)/2;
    v[h][mid] = to_string(root->val);
    chalochalo(root->left , si , mid - 1 , h + 1 , v);
    chalochalo(root->right, mid + 1 , ei , h + 1 , v);
}

vector<vector<string>> printTree(TreeNode *root)
{
    int h = getheight(root);
    int r = h;
    int c = pow(2, h) - 1;
    vector<vector<string>> v(r, vector<string>(c, ""));
    chalochalo(root, 0, c - 1, 0, v);
    return v;
}
};
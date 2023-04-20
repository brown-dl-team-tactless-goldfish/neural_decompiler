class Solution
{
public:
    void inorder(TreeNode *root, vector<int> &v)
    {
        if (root == nullptr)
            return;
        inorder(root->left, v);
        v.push_back(root->val);
        inorder(root->right, v);
    }
    vector<vector<int>> closestNodes(TreeNode *root, vector<int> &queries)
    {
        vector<vector<int>> ans;
        vector<int> v;
        inorder(root, v);
        for (auto &x : queries)
        {
            auto it = lower_bound(v.begin(), v.end(), x);
            if ((it != v.end()) && (*it == x))
            {
                ans.push_back({x, x});
            }
            else
            {
                int a = (it == v.begin()) ? -1 : *prev(it);
                int b = (it == v.end()) ? -1 : *it;
                ans.push_back({a, b});
            }
        }
        return ans;
    }
};
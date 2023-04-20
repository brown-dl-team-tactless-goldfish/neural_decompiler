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
    TreeNode* replaceValueInTree(TreeNode* root) {
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while(q.size()) {
            int n = q.size(), levelSum = 0;
            vector<pair<TreeNode*, int>> v;
            
            for(int i=0; i<n; i++) {
                TreeNode* temp = q.front().first;
                int value = q.front().second; q.pop();
                v.push_back({temp, value});

                if(temp -> left) levelSum += temp -> left -> val;
                if(temp -> right)  levelSum += temp -> right -> val;
            }
            for(int i=0; i<n; i++) {
                TreeNode* temp = v[i].first;
                int value = v[i].second;
                
                if(temp -> left) {
                    q.push({temp -> left, levelSum - temp -> left -> val - (temp -> right ? temp -> right -> val : 0)});
                }
                if(temp -> right) {
                    q.push({temp -> right, levelSum - temp -> right -> val - (temp -> left ? temp -> left -> val : 0)});
                }
                temp -> val = value;
            }
        }
        return root;
    }
};
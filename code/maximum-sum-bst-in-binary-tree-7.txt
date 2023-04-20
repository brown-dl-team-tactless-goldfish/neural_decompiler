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
    int ans=0;
public:
    pair<bool,pair<int,pair<int,int>>> sumFinder(TreeNode*root){
        if(!root){
            return {true,{0,{INT_MAX,INT_MIN}}};
        }
        pair<bool,pair<int,pair<int,int>>>l=sumFinder(root->left);
        pair<bool,pair<int,pair<int,int>>>r=sumFinder(root->right);
        
        int temp=root->val;
        bool flag=false;
        
        if(l.first&&r.first&&(!root->left||root->left->val<root->val)&&(!root->right||root->right->val>root->val)&&temp>l.second.second.second&&temp<r.second.second.first){
            flag=true;
            temp+=l.second.first+r.second.first;
        }
        if(flag)
            ans=max(ans,temp);
        return {flag,{temp,{min(root->val,l.second.second.first),max(root->val,r.second.second.second)}}};
    }
    int maxSumBST(TreeNode* root) {
        pair<bool,pair<int,pair<int,int>>>p=sumFinder(root);
        return ans;
    }
};
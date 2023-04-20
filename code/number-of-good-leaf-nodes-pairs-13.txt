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
      vector<TreeNode*>leafs;
unordered_map<TreeNode*,TreeNode*>mp;

int countPairs(TreeNode* root, int distance) 
{	
     fillmap(root);
     
     int count=0;
     unordered_set<TreeNode*>st;
	  
     for(int i=0;i<leafs.size();i++)
     {
     	dfs(leafs[i],st,distance,0,count);
     	st.clear();
	 }
	
	 return count/2;
}
void dfs(TreeNode* node,unordered_set<TreeNode*>&st,int &distance,int dis,int &count)
{
	if(node==NULL)
	return;
	
	if(dis > distance)
	return;
	
	if(st.find(node)!=st.end())
	return;
	
	if(dis <= distance and node!=NULL and node->left==NULL and node->right==NULL and dis!=0)  
    {
      count++;
    }
	
	
	st.insert(node);
	
	dfs(node->left,st,distance,dis+1,count);
	dfs(node->right,st,distance,dis+1,count);
	dfs(mp[node],st,distance,dis+1,count);
	
}
void fillmap(TreeNode* root)
{
   if(root==NULL)
   return;
   
   if(root!=NULL and root->left==NULL and root->right==NULL)
   {
      leafs.push_back(root);	
   }	
   
   if(root!=NULL and root->left!=NULL)
   {
   	 mp[root->left]=root;
   }
   if(root!=NULL and root->right!=NULL)
   {
   	 mp[root->right]=root;
   }
   fillmap(root->left);
   fillmap(root->right);
}
};
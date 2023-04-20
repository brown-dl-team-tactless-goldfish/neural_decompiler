struct TreeNode* searchBST(struct TreeNode* root, int val){
    if (!root || root->val == val)
		return root;
	
    if (root->val < val)
		return searchBST(root->right, val);
    else
		return searchBST(root->left, val);
}
int getSize(struct TreeNode* root)
{
    if (root == NULL)
    {
        return 0;
    }
    
    return 1+ getSize(root->left) + getSize(root->right);
}

void treeToArray(struct TreeNode* root , int* arra, int* index)
{
    if (root == NULL)
    {
        return; 
    }
    treeToArray(root->left, arra, index);
    arra[*index] = root->val;
    
    *index += 1;
    
    treeToArray(root->right, arra, index);
    
    
    return;
    
    
}


int minDiffInBST(struct TreeNode* root)
{
    int size = getSize(root);
    
    int arra[size];
    
    int index = 0;
    
    treeToArray(root, arra, &index);
    
    int mindiff = INT_MAX;
    int currentdiff = 0;
    for (int i = 1; i <size; i++)
    {
        
        currentdiff= arra[i] - arra[i-1];
        
        if (currentdiff < mindiff)
        {
            mindiff = currentdiff;
        }
    }
    
    
    return mindiff;
    

}
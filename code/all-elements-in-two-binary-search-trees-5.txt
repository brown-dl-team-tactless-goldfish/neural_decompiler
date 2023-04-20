/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void inorder(struct TreeNode*root,int **arr,int *as) {
    if(root->left) inorder(root->left,arr,as);
    (*arr) = (int*)realloc((*arr),++(*as)*sizeof(int));
    (*arr)[(*as)-1]=root->val;
    if(root->right) inorder(root->right,arr,as);
}
void merge(int *arr1,int as1,int *arr2,int as2,int *res) {
    int i=0,j=0,k=0;
    while(i<as1 && j <as2) {
        if(arr1[i]<arr2[j]) res[k] = arr1[i++];
        else res[k] = arr2[j++];
        k++;
    }
    while(i<as1) res[k++] = arr1[i++];
    while(j<as2) res[k++] = arr2[j++];
}
int* getAllElements(struct TreeNode* root1, struct TreeNode* root2, int* returnSize){
    int *res = NULL;
    int *arr1 = NULL;
    int *arr2 = NULL;
    int as1=0,as2=0;
    if(root1)inorder(root1,&arr1,&as1);
    if(root2)inorder(root2,&arr2,&as2);
    
    (*returnSize) = as1+as2;
    res = (int*)malloc((*returnSize)*sizeof(int));
    merge(arr1,as1,arr2,as2,res);
    free(arr1);
    free(arr2);
    return res;
}
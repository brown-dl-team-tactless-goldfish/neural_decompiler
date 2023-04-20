/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int count_nodes(struct TreeNode * root)
{
    if(root == NULL)
        return 0;
    
    return (1+count_nodes(root->left)+count_nodes(root->right));
}

void inorder(struct TreeNode * root, int * ret_arr, int * ret_arr_index)
{
    if(root==NULL)
        return;
    
    inorder(root->left, ret_arr, ret_arr_index);
    ret_arr[(*ret_arr_index)++] = root->val;
    inorder(root->right, ret_arr, ret_arr_index);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getAllElements(struct TreeNode* root1, struct TreeNode* root2, int* returnSize)
{

    int nodes1 = count_nodes(root1);
    int nodes2 = count_nodes(root2);
    
    int * ret_arr = (int *)malloc(sizeof(int) * (nodes1 + nodes2));
    int ret_arr_index = 0;
    
    int * arr1 = (int *)malloc(sizeof(int) * nodes1);
    int arr1_index = 0;
    int * arr2 = (int *)malloc(sizeof(int) * nodes2);
    int arr2_index = 0;
    
    inorder(root1, arr1, &arr1_index);
    inorder(root2, arr2, &arr2_index);
    
    
    int i=0, j=0;
    for(i=0,j=0; i<arr1_index && j<arr2_index; )
    {
        if(arr1[i] <=arr2[j])
        {
            ret_arr[ret_arr_index++] = arr1[i];
            i++;
        }
        else
        {
            ret_arr[ret_arr_index++] = arr2[j];
            j++;
        }
    }
    
    while(i<arr1_index)
    {
         ret_arr[ret_arr_index++] = arr1[i];
         i++;
    }
    
    while(j<arr2_index)
    {
        ret_arr[ret_arr_index++] = arr2[j];
        j++;
    }
    
    *returnSize = ret_arr_index;
    return ret_arr;
}
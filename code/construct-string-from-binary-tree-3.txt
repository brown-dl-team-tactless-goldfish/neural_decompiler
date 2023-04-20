/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <stdlib.h>
#include <string.h>

#define MAX_NODES 10000

int count_nodes(struct TreeNode * root)
{
    if(root == NULL)
        return 0;
    
    return (1 + count_nodes(root->left) + count_nodes(root->right));
}

void preorder(struct TreeNode * root, char * ret_arr, int * ret_arr_index)
{
    if(root==NULL)
    {
        return;
    }
    
    char int_buf[5];
    sprintf(int_buf, "%d", root->val);

    int i=0;
    while(int_buf[i]!='\0')
    {
        ret_arr[(*ret_arr_index)++] = int_buf[i];
        i++;
    }
    
    if((root->left==NULL) && (root->right!=NULL))
    {
        ret_arr[(*ret_arr_index)++] = '(';
        ret_arr[(*ret_arr_index)++] = ')';
        ret_arr[(*ret_arr_index)++] = '(';
    }
    else if((root->left!=NULL) && (root->right==NULL))
    {
        ret_arr[(*ret_arr_index)++] = '(';
    }
    else if((root->left!=NULL) && (root->right!=NULL))
    {
        ret_arr[(*ret_arr_index)++] = '(';
    }
    
    preorder(root->left, ret_arr, ret_arr_index);
    
    if((root->left==NULL) && (root->right!=NULL))
    {
        preorder(root->right, ret_arr, ret_arr_index);
    }
    else if(root->right != NULL)
    {
        ret_arr[(*ret_arr_index)++] = '(';
        preorder(root->right, ret_arr, ret_arr_index);
    }
    
    ret_arr[(*ret_arr_index)++] = ')';
}

char * tree2str(struct TreeNode* root)
{
    int nodes = count_nodes(root);
    char * ret_arr = (char *)malloc(sizeof(char) *( (10*nodes) + 1));
    int ret_arr_index = 0;
    
    preorder(root, ret_arr, &ret_arr_index);
    ret_arr[--ret_arr_index] = '\0';
    return ret_arr;
}
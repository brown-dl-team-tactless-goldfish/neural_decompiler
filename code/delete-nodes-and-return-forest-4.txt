/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void delete_element(int del_val, struct TreeNode ** ret_arr, int * ret_arr_index)
{
    int i=0;
    for(i=0; i<*ret_arr_index; i++)
    {
        if(ret_arr[i]->val == del_val)
        {
            //Shift the remaining elements
            int j=0;
            for(j=i; j<*ret_arr_index-1;j++)
            {
                ret_arr[j] = ret_arr[j+1];
            }
            *ret_arr_index -= 1;
            break;
        }
    }
}


struct TreeNode * del_node(struct TreeNode * root, int del_val, struct TreeNode ** ret_arr, int * ret_arr_index, bool * del_element_found)
{
    if(root == NULL)
    {
        return NULL;
    }
    
    if(root->val == del_val)
    {
        if((root->left == NULL) && (root->right == NULL))
        {
            //If the element is in return list delete the element
            delete_element(del_val, ret_arr, ret_arr_index);
            
            free(root);
            *del_element_found = true;
            
            
            
            return NULL;
        }
        else if((root->left != NULL) && (root->right == NULL))
        {   
            //If the element is in return list delete the element
            delete_element(del_val, ret_arr, ret_arr_index);
            
            ret_arr[*ret_arr_index] = root->left;
            *ret_arr_index += 1;
            free(root);
            *del_element_found = true;
            return NULL;
            
        }
        else if((root->left == NULL) && (root->right != NULL))
        {
            //If the element is in return list delete the element
            delete_element(del_val, ret_arr, ret_arr_index);
            
            ret_arr[*ret_arr_index] = root->right;
            *ret_arr_index += 1;
            free(root);
            *del_element_found = true;
            return NULL;
        }
        else if((root->left != NULL) && (root->right != NULL))
        {
            //If the element is in return list delete the element
            delete_element(del_val, ret_arr, ret_arr_index);
            
            ret_arr[*ret_arr_index] = root->left;
            *ret_arr_index += 1;
            
            ret_arr[*ret_arr_index] = root->right;
            *ret_arr_index += 1;
            free(root);
            *del_element_found = true;
            return NULL;
        }
    }
    
    root->left = del_node(root->left, del_val, ret_arr, ret_arr_index, del_element_found);
    root->right = del_node(root->right, del_val, ret_arr, ret_arr_index, del_element_found);
    return root;
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TreeNode** delNodes(struct TreeNode* root, int* to_delete, int to_deleteSize, int* returnSize)
{
    struct TreeNode * root_node = root;
    
    struct TreeNode ** ret_arr = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * (2*to_deleteSize + 1));
    int ret_arr_index = 0;
    bool root_del = false;
    int i=0;
    for(i=0; i<to_deleteSize; i++)
    {
        if(root->val == to_delete[i])
        {
            root_del = true;
            break;
        }
    }
    int isrootdeleted = false;
    
    for(i=0; i<to_deleteSize; i++)
    {
        bool del_element_found = false;
        int del_val = to_delete[i];

        
        if(isrootdeleted == false)
        {
            if(del_val == root_node->val)
            {
                isrootdeleted = true;
            }
            
            del_node(root, del_val, ret_arr, &ret_arr_index, &del_element_found);
            printf("%d\r\n", del_element_found);
            if(del_element_found == false)
            {
                int j=0;
                for(j=0; j<ret_arr_index; j++)
                {
                    del_node(ret_arr[j], del_val, ret_arr, &ret_arr_index, &del_element_found);
                
                    if(del_element_found)
                    {
                        break;
                    }
                }
            }
        }
        else if(isrootdeleted == true)
        {
            int j=0;
            for(j=0; j<ret_arr_index; j++)
            {
                del_node(ret_arr[j], del_val, ret_arr, &ret_arr_index, &del_element_found);
                
                if(del_element_found)
                {
                    break;
                }
            }
               
        }
        
        
    }
    
    if(root_del == false)
    {
        ret_arr[ret_arr_index++] = root; 
    }
    
    *returnSize = ret_arr_index;
    return ret_arr;
}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void check_palindrone( int * pseudo_count, uint16_t * number, int * elements_count)
{
    int i=0;
    bool match = true;
    
    
    if((*elements_count)%2 == 0)   //Even number of elements
    {

        //If the is any of the odd element entry then its not possible to get a palindrone out of it
        if(*number == 0x00)
        {
            
            match = true;
        }
        else
        {
            match = false;
        }
    }
    else    //Odd Number of elements
    {
        int j=0;
        int odd_elements = 0;
        for(j=0; j<10; j++)
        {
            if(((*number)>>j & 0x01 == 1))
            {
                odd_elements++;
            }
            
            if(odd_elements > 1)
            {
                match = false;
                break;
            }
        }
        
    }
    
    if(match == true)
    {
        *pseudo_count += 1;
    }
}

void preorder(struct TreeNode * root, int * pseudo_count, uint16_t * number, int * elements_count)
{
    if(root == NULL)
        return;
    
    //Set the bit of the number
    *number = *number ^ (0x01 << root->val);
    *elements_count += 1;
    
    if((root->left == NULL) && (root->right == NULL))
    {
        check_palindrone(pseudo_count, number, elements_count);
    }
    
    preorder(root->left, pseudo_count, number, elements_count);
    preorder(root->right,  pseudo_count, number, elements_count);
    
    *number = *number ^ (0x01 << root->val);
    *elements_count -= 1;
}

int pseudoPalindromicPaths (struct TreeNode* root)
{   
    uint16_t number = 0x00;
    
    int pseudo_count = 0;
    int elements_count = 0;
    
    preorder(root, &pseudo_count, &number, &elements_count);
    return pseudo_count;
}
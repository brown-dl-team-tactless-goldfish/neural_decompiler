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
    
    return (1 + count_nodes(root->left) + count_nodes(root->right));
}

void merge(int arr[], int low, int mid, int high)
{
    int * ret_arr = (int *)malloc(sizeof(int) * (high - low + 1));
    int ret_arr_index = 0;
    
    int i=0,j=0;
    for(i=low, j=mid+1; i<=mid && j<=high; )
    {
        if(arr[i] <= arr[j])
        {
            ret_arr[ret_arr_index++] = arr[i++];
        }
        else
        {
            ret_arr[ret_arr_index++] = arr[j++];
        }
    }
    
    while(i<=mid)
    {
        ret_arr[ret_arr_index++] = arr[i++];
    }
    
    while(j<=high)
    {
        ret_arr[ret_arr_index++] = arr[j++];
    }
    
    memcpy(&arr[low], ret_arr, sizeof(int) * ret_arr_index);
}

int tree_traversal(struct TreeNode * root, int * ret_arr, int * ret_arr_index)
{
    if(root == NULL)
        return 0;
    
    if(root->left==NULL && root->right==NULL)
    {
        ret_arr[(*ret_arr_index)++] = root->val;
        return root->val;
    }
    
    int left = tree_traversal(root->left, ret_arr, ret_arr_index);
    int right = tree_traversal(root->right, ret_arr, ret_arr_index);
    int sum = left + right + root->val;
    
    ret_arr[(*ret_arr_index)++] = sum;
    return sum;
}

void merge_sort(int arr[], int low, int high)
{
    if(low<high)
    {
        int mid = (low+high)/2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findFrequentTreeSum(struct TreeNode* root, int* returnSize)
{
    int no_of_nodes = count_nodes(root);
    
    int * ret_arr = (int *)malloc(sizeof(int) * no_of_nodes);
    int ret_arr_index = 0;
    
    int sum = tree_traversal(root, ret_arr, &ret_arr_index);
    
    //Sort the ret_arr using merge sort
    merge_sort(ret_arr, 0, ret_arr_index-1);
    int i=0;   
    
    int max = INT_MIN;
    int count = 0;
    int prev = ret_arr[0];
    for(i=0; i<ret_arr_index; )
    {
        if(prev == ret_arr[i])
        {
            i++;
            count++;
            
            if(count >= max)
                max = count;
        }
        else
        {
            if(count >= max)
                max = count;
            count = 0;
            prev = ret_arr[i];
        }
    }
    
    
    int * new_arr = (int *)malloc(sizeof(int) * no_of_nodes);
    int new_arr_index = 0;
    count = 0;
    prev = ret_arr[0];

     for(i=0; i<ret_arr_index; )
    {
        if(prev == ret_arr[i])
        {
            count++;
            
            if(max == count)
            {
                new_arr[new_arr_index++] = ret_arr[i];
            }
            i++;
        }
        else
        {
            count = 0;
            prev = ret_arr[i];
        }
    }
    
    
    
    *returnSize = new_arr_index;
    return new_arr;
}
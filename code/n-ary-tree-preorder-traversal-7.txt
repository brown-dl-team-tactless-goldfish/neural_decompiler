/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void tree2arr(struct Node* root,int* arr, int* returnSize){
    if(root){
        arr[(*returnSize)++] = root->val;
        for(int i = 0; i < root->numChildren; i++){
            tree2arr(root->children[i], arr, returnSize);
        }
    }
}
int* preorder(struct Node* root, int* returnSize) {
    int* arr = malloc(sizeof(int)*10000);
    *returnSize =0;
    tree2arr(root, arr, returnSize);
    return arr;
    
}
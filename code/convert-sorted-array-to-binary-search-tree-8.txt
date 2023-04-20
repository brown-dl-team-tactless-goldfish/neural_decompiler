struct TreeNode *sortedArrayToBST(int *nums, int numsSize)
{
    if (numsSize == 0)
    {
        return NULL;
    }
    int midIndex = numsSize >> 1;
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->val = nums[midIndex];
    node->left = sortedArrayToBST(&nums[0], midIndex);
    node->right = sortedArrayToBST(&nums[midIndex + 1], numsSize - midIndex - 1);
    return node;
}
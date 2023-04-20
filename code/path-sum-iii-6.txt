/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define STACK_SIZE  1000

int count = 0;

typedef struct
{
    struct TreeNode * arr[STACK_SIZE];
    int top;
}Stack;

int isStackFull(Stack * tmp_stack)
{
    if(tmp_stack->top == STACK_SIZE-1)
        return 1;
    else
        return 0;
}

int isStackEmpty(Stack * tmp_stack)
{
    if(tmp_stack->top == -1)
        return 1;
    else
        return 0;
}

void push(Stack * tmp_stack, struct TreeNode * element)
{
    if(isStackFull(tmp_stack))
        return;
    
    tmp_stack->arr[++(tmp_stack->top)] = element;
}

struct TreeNode * pop(Stack * tmp_stack)
{
    if(isStackEmpty(tmp_stack))
        return NULL;
    
    return tmp_stack->arr[(tmp_stack->top)--];
}

int peek(Stack * tmp_stack, int index)
{
    if(isStackEmpty(tmp_stack))
        return INT_MIN;
    
    return tmp_stack->arr[index]->val;
}

void preorder(struct TreeNode * root, Stack * tmp_stack, int target, int * count)
{
    if(root == NULL)
        return;
    
    push(tmp_stack, root);
    
    
    //Check whether possible path exists
    int i=tmp_stack->top;
    int current_sum = 0;
    while(1)
    {
        current_sum += peek(tmp_stack, i);
        
        if(current_sum == target)
        {
            *count += 1;
        }
        
        i--;
        if(i<0)
        {
            break;
        }
    }
    
    //Go to left child
    preorder(root->left, tmp_stack, target, count);
    
    preorder(root->right, tmp_stack, target, count);
    
    struct TreeNode * pop_element = pop(tmp_stack);
    return;
}

int pathSum(struct TreeNode* root, int targetSum)
{
    
    Stack tmp_stack;
    tmp_stack.top = -1;
    
    
    count = 0;
    preorder(root, &tmp_stack, targetSum, &count);
    return count;
    
    
}
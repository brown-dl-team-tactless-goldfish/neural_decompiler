/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define MAX_ELEMENTS 100
#define TREE_MAX_ELEMENTS 2500

struct TreeNode * tree_arr[TREE_MAX_ELEMENTS] = {NULL};

typedef struct
{
    struct ListNode * arr[MAX_ELEMENTS];
    int top;
}Stack;

int isStackFull(Stack * tmp_stack)
{
    if(tmp_stack->top == MAX_ELEMENTS-1)
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

void push(Stack * tmp_stack, struct ListNode * element)
{
    if(isStackFull(tmp_stack))
        return;
    tmp_stack->arr[++(tmp_stack->top)] = element;
}

struct ListNode * pop(Stack * tmp_stack)
{
    if(isStackEmpty(tmp_stack))
        return NULL;
    return tmp_stack->arr[(tmp_stack->top)--];
}


void preorder(struct ListNode * head, struct TreeNode * root, Stack * tmp_stack, bool * result)
{
    if(root == NULL)
        return;
    
    if(root->val == head->val)
    {
        push(tmp_stack, head);
        
        if(head->next == NULL)
        {
            *result = true;
            return;
        }
        
        preorder(head->next, root->left, tmp_stack, result);
        
        if(isStackEmpty(tmp_stack))
        {
            push(tmp_stack, head);
        }
        
        preorder(head->next, root->right, tmp_stack, result);
        struct ListNode * pop_node = pop(tmp_stack);
    }
    else
    {
        while(!isStackEmpty(tmp_stack))
        {
           struct ListNode * pop_node = pop(tmp_stack);
           if(isStackEmpty(tmp_stack))
           {
               head = pop_node;
           }
        }
        if(root->val == head->val)
        {
            preorder(head, root, tmp_stack, result);
        }
        else
        {
            preorder(head, root->left, tmp_stack, result);
            preorder(head, root->right, tmp_stack, result);
        }
    }
}

void head_root_find(struct ListNode* head, struct TreeNode* root, int * ret_index)
{
   if(root == NULL)
       return;
    
    if(root->val == head->val)
    {
        tree_arr[*ret_index] = root;
        *ret_index += 1;
    }
    head_root_find(head, root->left, ret_index);
    head_root_find(head, root->right, ret_index);
    
}

bool isSubPath(struct ListNode* head, struct TreeNode* root)
{
    bool result = false;
    Stack tmp_stack;
    tmp_stack.top = -1;
    
    memset(tree_arr, NULL, sizeof(tree_arr));
    int ret_index = 0;
    
    int i=0;
    head_root_find(head, root, &ret_index);
    
    for(i=0; i<ret_index; i++)
    {
        preorder(head, tree_arr[i], &tmp_stack, &result);
        
        if(result == true)
            break;
    }
    return result;
    
}
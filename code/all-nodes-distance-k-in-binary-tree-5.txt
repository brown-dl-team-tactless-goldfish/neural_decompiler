/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define TOTAL_NODES 501

typedef struct
{
    struct TreeNode * arr[TOTAL_NODES];
    int levels[TOTAL_NODES];
    int front;
    int rear;
}Queue;

int isQueueEmpty(Queue * tmp_queue)
{
    if(tmp_queue->front == -1)
        return 1;
    else
        return 0;
}

int isQueueFull(Queue * tmp_queue)
{
    if(tmp_queue->rear == TOTAL_NODES-1)
        return 1;
    else
        return 0;
}

void enqueue(Queue * tmp_queue, struct TreeNode * element, int level)
{
    if(isQueueFull(tmp_queue))
        return;
    
    tmp_queue->arr[++(tmp_queue->rear)] = element;
    tmp_queue->levels[tmp_queue->rear] = level;
    
    if(tmp_queue->front == -1)
        tmp_queue->front = 0;
}

struct TreeNode * dequeue(Queue * tmp_queue, int * level)
{
    if(isQueueEmpty(tmp_queue))
        return NULL;
    
    *level =  tmp_queue->levels[tmp_queue->front];
    struct TreeNode * ret = tmp_queue->arr[tmp_queue->front];
    
    if(tmp_queue->front == tmp_queue->rear)
    {
        tmp_queue->front = -1;
        tmp_queue->rear = -1;
    }
    else
    {
        (tmp_queue->front)++;
    }
    return ret;
}


int count_nodes(struct TreeNode * root)
{
    if(root == NULL)
    {
        return 0;
    }
    
    return (1 + count_nodes(root->left) + count_nodes(root->right));
}

void traversal(struct TreeNode * root, struct TreeNode ** hashtable)
{
    if(root == NULL)
        return;
    
    if(root->left != NULL)
    {
        hashtable[root->left->val] = root;
    }
    
    if(root->right != NULL)
    {
        hashtable[root->right->val] = root;
    }
    
    traversal(root->left, hashtable);
    traversal(root->right, hashtable);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* distanceK(struct TreeNode* root, struct TreeNode* target, int k, int* returnSize) 
{
    //To find the distance k from target, we need to go down k distance from target downwards as well as k distance upwards (towards parent). Since in binary tree we cannot
    //traverse or have information about parent readily, we need to do a DFS and create a hashtable containing parent child values.
    int no_of_nodes = count_nodes(root);
    
    struct TreeNode  ** hashtable = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * TOTAL_NODES);
    memset(hashtable, NULL, sizeof(struct TreeNode *) * no_of_nodes);

    hashtable[root->val] = NULL;    //Root has no parent
    traversal(root, hashtable);
    
    //Once the hashtable is created and we have the knowledge of parents, we do a BFS level by lavel to arrive to the nodes at a particular level.
    //Also we maintain another hashtable called seen_hashtable to eliminate the inclusion of duplicates node. For ex. in BFS we can insert B which is child of A and while 
    //processing B we shouldn't include the parent A as we have already processed the parent. Hence we need a hashtable to eliminate this duplication.
    bool * seen_hashtable = (bool *)malloc(sizeof(bool) * TOTAL_NODES);
    int i=0;
    for(i=0; i<no_of_nodes; i++)
    {
        seen_hashtable[i] = false;
    }
    
    Queue tmp_queue;
    tmp_queue.front = -1;
    tmp_queue.rear = -1;
    
    int * ret_arr = (int *)malloc(sizeof(int) * no_of_nodes);
    int ret_arr_index = 0;
    
    struct TreeNode * tmp_ptr = target;
    int current_level = 0;
    enqueue(&tmp_queue, tmp_ptr, current_level);
    seen_hashtable[target->val] = true;
    
    
    while(!isQueueEmpty(&tmp_queue))
    {     
        tmp_ptr = dequeue(&tmp_queue, &current_level);
        if(current_level != k)
        {
            //Insert left child
            if(tmp_ptr->left!=NULL)
            {
                if(seen_hashtable[tmp_ptr->left->val] == false)
                {
                    enqueue(&tmp_queue, tmp_ptr->left, current_level+1);
                    seen_hashtable[tmp_ptr->left->val] = true;
                }
            }
            
            //Insert right child
            if(tmp_ptr->right!=NULL)
            {
                if(seen_hashtable[tmp_ptr->right->val] == false)
                {
                    enqueue(&tmp_queue, tmp_ptr->right, current_level+1);
                    seen_hashtable[tmp_ptr->right->val] = true;
                }
            }
            
            //Insert parent
            struct TreeNode * parent = hashtable[tmp_ptr->val];
            if(parent != NULL)
            {
                if(seen_hashtable[parent->val] == false)
                {
                    enqueue(&tmp_queue, parent, current_level+1);
                    seen_hashtable[parent->val] = true;
                }
            }
                       
        }
        else if(current_level == k)
        {
            ret_arr[ret_arr_index++] = tmp_ptr->val;
        }
    }
    *returnSize = ret_arr_index;
    return ret_arr;

}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define MAX_NODES 200

typedef struct
{
    struct TreeNode * queue_arr[MAX_NODES];
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
    if(tmp_queue->rear == MAX_NODES-1)
        return 1;
    else
        return 0;
}

void enqueue(Queue * tmp_queue, struct TreeNode * element)
{
    if(isQueueFull(tmp_queue))
        return;
    
    tmp_queue->queue_arr[++(tmp_queue->rear)] = element;
    if(tmp_queue->front == -1)
    {
        tmp_queue->front = 0;
    }
    return;
}

struct TreeNode * dequeue(Queue * tmp_queue)
{
    if(isQueueEmpty(tmp_queue))
        return NULL;
    
    struct TreeNode * ret_element = tmp_queue->queue_arr[(tmp_queue->front)];
    
    if(tmp_queue->front == tmp_queue->rear)
    {
        tmp_queue->front = -1;
        tmp_queue->rear = -1;
    }
    else
    {
        ++(tmp_queue->front);
    }
    return ret_element;
}

bool isCompleteTree(struct TreeNode* root)
{
    int * arr = (int *)malloc(sizeof(int) * MAX_NODES);
    int arr_index = 0;
    
    struct TreeNode * tmp_ptr = root;
    Queue tmp_queue;
    tmp_queue.front = -1;
    tmp_queue.rear = -1;
    
    enqueue(&tmp_queue, tmp_ptr);
    bool match = true;
    bool no_child = false;
    
    while(!isQueueEmpty(&tmp_queue))
    {
        tmp_ptr = dequeue(&tmp_queue);
        
        if(tmp_ptr == NULL)
        {
            no_child = true;
            continue;
        }
        
        if(no_child == true && tmp_ptr != NULL)
        {
            match = false;
            break;
        }
        
        if(tmp_ptr->left != NULL && tmp_ptr->right != NULL)
        {
            enqueue(&tmp_queue, tmp_ptr->left);
            enqueue(&tmp_queue, tmp_ptr->right);
        }
        else if(tmp_ptr->left != NULL && tmp_ptr->right == NULL)
        {
            enqueue(&tmp_queue, tmp_ptr->left);
            enqueue(&tmp_queue, NULL);
        }
        else if(tmp_ptr->left == NULL && tmp_ptr->right != NULL)
        {
            match = false;
            break;
        }
        else
        {
            enqueue(&tmp_queue, NULL);
            enqueue(&tmp_queue, NULL);
        }
    }
    return match;
}
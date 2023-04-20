/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define MAX_QUEUE_SIZE 10000

typedef struct queue
{
    struct TreeNode * arr[MAX_QUEUE_SIZE];
    int level_arr[MAX_QUEUE_SIZE];
    int rear;
    int front;
}Queue;

int isQueueFull(Queue * level_sum_queue)
{
    if(level_sum_queue->rear == MAX_QUEUE_SIZE - 1)
        return 1;
    else
        return 0;
}

int isQueueEmpty(Queue * level_sum_queue)
{
    if(level_sum_queue->front == -1)
        return 1;
    else
        return 0;
}

void enqueue(Queue * level_sum_queue, struct TreeNode * element, int level_element)
{
    if(isQueueFull(level_sum_queue))
        return;
    
    level_sum_queue->arr[++(level_sum_queue->rear)] = element;
    level_sum_queue->level_arr[level_sum_queue->rear] = level_element;
    
    if(level_sum_queue->front == -1)
    {
        level_sum_queue->front = 0;
    }
    return;
}

struct TreeNode * dequeue(Queue * level_sum_queue, int * ret_level)
{
    if(isQueueEmpty(level_sum_queue))
    {
        *ret_level = 0;
        return NULL;
    }
    
    struct TreeNode * ret_element = level_sum_queue->arr[level_sum_queue->front];
    *ret_level = level_sum_queue->level_arr[level_sum_queue->front];
    
    if(level_sum_queue->front == level_sum_queue->rear)
    {
        level_sum_queue->front = -1;
        level_sum_queue->rear = -1;
    }
    else
    {
        ++(level_sum_queue->front);
    }
    return ret_element;
}

int maxLevelSum(struct TreeNode* root)
{
    Queue level_sum_queue;
    level_sum_queue.rear = -1;
    level_sum_queue.front = -1;
    memset(level_sum_queue.arr, NULL, sizeof(level_sum_queue.arr));
    memset(level_sum_queue.level_arr, 0, sizeof(level_sum_queue.level_arr));
    
    int current_level = 1;
    int prev_level = 0;
    int cur_sum = INT_MIN;
    int smallest_level = 0;
    int max_sum = INT_MIN;
    
    struct TreeNode * trav_ptr = root;
    
    enqueue(&level_sum_queue, trav_ptr, current_level);
    
    while(!isQueueEmpty(&level_sum_queue))
    {
        trav_ptr = dequeue(&level_sum_queue, &current_level);
        
        if(current_level != prev_level)
        {
            if(cur_sum > max_sum)
            {
                max_sum = cur_sum;
                smallest_level = prev_level;
            }
            
            cur_sum = 0;
            cur_sum = trav_ptr->val;
        }
        else
        {
            cur_sum += trav_ptr->val;
        }
        prev_level = current_level;
        
        
        if(trav_ptr->left != NULL)
        {
            enqueue(&level_sum_queue, trav_ptr->left, current_level+1);
        }
        
        if(trav_ptr->right != NULL)
        {
            enqueue(&level_sum_queue, trav_ptr->right, current_level+1);
        }
    }
    
    if(cur_sum > max_sum)
    {
        max_sum = cur_sum;
        smallest_level = current_level;
    }
    return smallest_level;

}
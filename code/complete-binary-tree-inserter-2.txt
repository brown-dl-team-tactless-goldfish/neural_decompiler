/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define MAX_NODES 1000
typedef struct
{
    struct TreeNode ** queue_arr;
    int front;
    int rear;
}Queue;

int isQueueEmpty(Queue * tmp_queue)
{
    if(tmp_queue->front == -1)
    {
        return 1;
    }
    else
        return 0;
}

int isQueueFull(Queue * tmp_queue)
{
    if(tmp_queue->rear == MAX_NODES - 1)
    {
        return 1;
    }
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
    if(tmp_queue->rear == tmp_queue->front)
    {
        tmp_queue->rear = -1;
        tmp_queue->front = -1;
    }
    else
    {
        (tmp_queue->front)++;
    }
    return ret_element;
}


typedef struct 
{
    struct TreeNode * root;
    struct TreeNode * insert_node;
    Queue * queue;
} CBTInserter;


CBTInserter* cBTInserterCreate(struct TreeNode* root) 
{
    CBTInserter * obj = (CBTInserter *)malloc(sizeof(CBTInserter));
    obj->root = root;
    
    obj->queue = (Queue *)malloc(sizeof(Queue));
    obj->queue->queue_arr = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * MAX_NODES);
    obj->queue->front = -1;
    obj->queue->rear  = -1;
    
    //Add the tree information in the queue
    struct TreeNode * trav_ptr = root;
    enqueue(obj->queue, trav_ptr);
    trav_ptr = dequeue(obj->queue);
    
    while(trav_ptr->left != NULL && trav_ptr->right != NULL)
    {
        //Push both the child     
        if(trav_ptr->left != NULL)
        {
            enqueue(obj->queue, trav_ptr->left);
        }
        
        if(trav_ptr->right != NULL)
        {
            enqueue(obj->queue, trav_ptr->right);
        }
        
        trav_ptr = dequeue(obj->queue);
    }
    
    if(trav_ptr->left != NULL && trav_ptr->right == NULL)
    {
        enqueue(obj->queue, trav_ptr->left);
        obj->insert_node = trav_ptr;
    }
    
    if(trav_ptr->left == NULL && trav_ptr->right == NULL)
    {
        obj->insert_node = trav_ptr;
    }
    return obj;
}

int cBTInserterInsert(CBTInserter* obj, int v)
{
    struct TreeNode * new_node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    new_node->val = v;
    new_node->left = NULL;
    new_node->right = NULL;
    
    struct TreeNode * trav_ptr = obj->insert_node;
    
    if(trav_ptr->left == NULL)  //Insertion at the left
    {
        trav_ptr->left = new_node;
        enqueue(obj->queue, new_node);
    }
    else    //Insertion at the right
    {
        trav_ptr->right = new_node;
        enqueue(obj->queue, new_node);
        obj->insert_node = dequeue(obj->queue);
    }
    
    return trav_ptr->val;
}

struct TreeNode* cBTInserterGet_root(CBTInserter* obj) 
{
    return obj->root;
}

void cBTInserterFree(CBTInserter* obj) 
{
    free(obj);    
}

/**
 * Your CBTInserter struct will be instantiated and called as such:
 * CBTInserter* obj = cBTInserterCreate(root);
 * int param_1 = cBTInserterInsert(obj, v);
 
 * struct TreeNode* param_2 = cBTInserterGet_root(obj);
 
 * cBTInserterFree(obj);
*/